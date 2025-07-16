from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email address', validators=[DataRequired()])
    address = TextAreaField('Address')  # remains the same for free-form address input
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('Repeat Password',
                              validators=[DataRequired(), EqualTo('password', message="Passwords must match.")])
    community = SelectField('Community', choices=[], validators=[DataRequired()])  # Dropdown for community selection
    submit = SubmitField('Sign Up')

class ContributionForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    observation_type = SelectField(
        'Observation Type',
        choices=[
            ('population_update', 'Population Update'),
            ('threat_report', 'Threat Report'),
            ('general_observation', 'General Observation')
        ],
        validators=[DataRequired()]
    )
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    report = TextAreaField('Report', validators=[DataRequired()])
    community = SelectField('Your Community', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit Contribution')
