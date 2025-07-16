from flask import Blueprint, render_template, request
from models import Species
bp = Blueprint('species_routes', __name__, url_prefix='/species')

@bp.route('/')
def species():
    # For now, fetch all species.
    species_list = Species.query.all()
    return render_template('species.html', species=species_list)
