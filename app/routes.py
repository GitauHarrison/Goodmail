from app import app, db
from flask import render_template, url_for, flash, redirect
from app.forms import HomeForm

@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = HomeForm()
    if form.validate_on_submit():
        # user = User(email = form.email.data, site = form.site.data)
        # db.session.add(user)
        # db.session.commit()
        flash('Your data was saved successfully!')
    return render_template('home.html', title = 'Home', form = form)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')