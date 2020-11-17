from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import HomeForm

@app.route('/')
@app.route('/home')
def home():
    form = HomeForm()
    flash('This is a test message')
    return render_template('home.html', title = 'Home', form = form)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')