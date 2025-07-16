import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://adiand:ludo.1234@localhost/wildlife_in_a_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # New upload configuration
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}