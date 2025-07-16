from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models import Contributions, UserContributions, CommunitiesUsers
from forms import ContributionForm

bp = Blueprint('contribution_routes', __name__, url_prefix='/contribution')

@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_contribution():
    form = ContributionForm()
    if form.validate_on_submit():
        contribution = Contributions(
            Date=form.date.data,
            Image=form.image.data,
            ObservationType=form.observation_type.data,
            Report=form.report.data
        )
        db.session.add(contribution)
        db.session.commit()
        # Link the contribution to the user via the CommunitiesUsers aggregate
        cu = CommunitiesUsers.query.filter_by(User_ID=current_user.User_ID).first()
        if not cu:
            flash('User is not linked to a community. Contribution not recorded properly.')
            return redirect(url_for('main_routes.home'))
        user_contrib = UserContributions(Contribution_ID=contribution.Contribution_ID, CU_ID=cu.CU_ID)
        db.session.add(user_contrib)
        db.session.commit()
        flash('Contribution added successfully!')
        return redirect(url_for('user_routes.dashboard'))
    return render_template('contribution.html', form=form)
