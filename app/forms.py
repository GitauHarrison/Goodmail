from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class HomeForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    site = StringField('Site', validators=[DataRequired()], render_kw={"placeholder": "Site URL"})
    submit = SubmitField('Submit')