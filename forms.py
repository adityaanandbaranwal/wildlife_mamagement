from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email address', validators=[DataRequired()])
    address = TextAreaField('Region Address')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match.")])
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
    image = StringField('Image URL')
    report = TextAreaField('Report', validators=[DataRequired()])
    submit = SubmitField('Submit Contribution')
