# routes/contribution_routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request
from flask_login import login_required, current_user
from extensions import db
from models import Contributions
from forms import ContributionForm
from werkzeug.utils import secure_filename
import os
from sqlalchemy import text

bp = Blueprint('contribution_routes', __name__, url_prefix='/contribution')

def allowed_file(filename):
    # simple check for extension
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_contribution():
    form = ContributionForm()
    
    # Populate the community drop-down list (similar to before).
    community_region_list = db.session.execute(
        text('''
          SELECT c.Community_ID, c.CommunityName, r.State, r.City_Village
          FROM Communities c
          JOIN CommunityRegions cr ON c.Community_ID = cr.Community_ID
          JOIN Region r ON cr.Region_ID = r.Region_ID
        ''')
    ).fetchall()

    dropdown_options = [('None', 'None')]
    for row in community_region_list:
        label = f"{row.CommunityName} - {row.State}, {row.City_Village}"
        dropdown_options.append((str(row.Community_ID), label))
    form.community.choices = dropdown_options

    if form.validate_on_submit():
        # Process the file upload.
        image_path = None
        if form.image.data:
            file = form.image.data
            # Check if the file has an allowed extension.
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Save the file to the configured upload folder.
                upload_folder = current_app.config['UPLOAD_FOLDER']
                file_path = os.path.join(upload_folder, filename)
                file.save(file_path)
                
                # Store the relative path to the file (accessible via url_for('static', ...)).
                image_path = os.path.join('uploads', filename)
            else:
                flash('Invalid image file. Please upload a valid image.')
                return render_template('contribution.html', form=form)
        
        # Create the contribution record.
        contribution = Contributions(
            Date=form.date.data,
            Image=image_path,
            ObservationType=form.observation_type.data,
            Report=form.report.data,
            Contributor_ID=current_user.User_ID,
            ContributionCommunity=form.community.data  # either a valid community id or 'None'
        )
        db.session.add(contribution)
        db.session.commit()
        flash('Contribution added successfully!')
        return redirect(url_for('user_routes.dashboard'))
    return render_template('contribution.html', form=form)
