from flask import Blueprint, render_template, redirect, url_for, flash
from extensions import db
from models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from forms import LoginForm, SignupForm

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
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = Users(UserName=form.username.data,
                         Email_ID=form.email.data,
                         UserAddress=form.address.data,
                         PasswordHash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created. Please sign in.')
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
