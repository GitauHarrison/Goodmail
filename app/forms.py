from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class HomeForm(FlaskForm):
    email = StringField('Email', render_kw={"placeholder": "Your Email"})
    site = StringField('Site', render_kw={"placeholder": "Site URL"})
    submit = SubmitField('Submit')