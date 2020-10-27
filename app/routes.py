from app import app
from flask import Flask, render_template, redirect, url_for
from flask_login import login_required, current_user, logout_user



@app.route('/')
@app.route('/home')
def index():
    return render_template('base.html', title='YouLearn')