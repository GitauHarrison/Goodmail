from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

class HomeForm(FlaskForm):
    username = StringField('Your Name', validators=[DataRequired()], render_kw={"placeholder": "Your Name"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    site_url = StringField('Site', validators=[DataRequired()], render_kw={"placeholder": "Site URL"})
    submit = SubmitField('Submit')
