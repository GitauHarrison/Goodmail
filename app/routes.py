from app import app
from flask import render_template, url_for, flash, redirect

@app.route('/')
@app.route('/home')
def home():
    flash('This is a test message')
    return render_template('home.html', title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')