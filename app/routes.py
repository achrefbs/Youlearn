from app import app
from flask import Flask, render_template, redirect, url_for
from flask_login import login_required, current_user, logout_user



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='YouLearn')

@app.route('/settings')
def settings():
	profile = {'email':current_user.email,'name':current_user.name, 'lastname':current_user.lastname, 'telephone': current_user.telephone}
	return render_template('settings.html', title='Settings', profile=profile)


@app.route('/profile')
def profile():
	return render_template('profile.html', title='Profile')