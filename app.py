# First, apply the monkey patch.
import patch_werkzeug  # ensure this is in the project root and imported first

from flask import Flask
from config import Config
from extensions import db, login
# We are leaving out flask-migrate for now
# from flask_migrate import Migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)
    
    # Register blueprints
    from routes import main_routes, user_routes, species_routes, contribution_routes
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(species_routes.bp)
    app.register_blueprint(contribution_routes.bp)

    return app

app = create_app()

# Define the user loader for Flask-Login
from models import Users  # Import here to avoid circular dependencies
@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)
