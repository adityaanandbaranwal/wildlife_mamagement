from flask import Blueprint, render_template, redirect, url_for, flash, request
from extensions import db
from models import Contributions, Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from forms import LoginForm, SignupForm
from sqlalchemy import text

bp = Blueprint('user_routes', __name__, url_prefix='/user')

@bp.route('/signin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(Email_ID=form.email.data).first()
        if user and check_password_hash(user.PasswordHash, form.password.data):
            login_user(user)
            return redirect(url_for('main_routes.home'))
        else:
            flash('Invalid email or password')
    return render_template('signin.html', form=form)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    # Query to get community info from Communities and Region (via CommunityRegions join)
    community_region_list = db.session.execute(
    text('''
    SELECT c.Community_ID, c.CommunityName, r.State, r.City_Village
    FROM Communities c
    JOIN CommunityRegions cr ON c.Community_ID = cr.Community_ID
    JOIN Region r ON cr.Region_ID = r.Region_ID
    ''')
    ).fetchall()

    # Build the dropdown options: add an option for "None" first.
    dropdown_options = [('None', 'None')]
    for row in community_region_list:
        label = f"{row.CommunityName} - {row.State}, {row.City_Village}"
        dropdown_options.append((str(row.Community_ID), label))  # convert ID to string for consistency

    form = SignupForm()
    # Set the choices dynamically
    form.community.choices = dropdown_options

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        # Create a new user; note we store:
        # - The free-form address into UserAddress
        # - The selected community dropdown value into SelectedCommunity.
        new_user = Users(
            Email_ID=form.email.data,
            UserName=form.username.data,
            UserAddress=form.address.data,
            SelectedCommunity=form.community.data,  # contains the community ID or 'None'
            PasswordHash=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully.')
        return redirect(url_for('user_routes.login'))
    return render_template('signup.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_routes.home'))

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@bp.route('/my_contributions', methods=['GET'])
@login_required
def view_contributions():
    # Query contributions made by the current logged in user.
    contributions = Contributions.query.filter_by(Contributor_ID=current_user.User_ID).all()
    return render_template('dashboard_contributions.html', contributions=contributions)

@bp.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    if request.method == 'POST':
        # Delete the current user. Because foreign keys are set with ON DELETE CASCADE,
        # associated records in Community_User will be removed automatically.
        db.session.delete(current_user)
        db.session.commit()
        flash('Your account has been deleted.', 'info')
        logout_user()
        return redirect(url_for('main_routes.home'))
    # GET request: Render a confirmation page.
    return render_template('delete_account.html')