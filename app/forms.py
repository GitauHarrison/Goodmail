from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class HomeForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Your Username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    site_url = StringField('Site', validators=[DataRequired()], render_kw={"placeholder": "Site URL"})
    submit = SubmitField('Submit')