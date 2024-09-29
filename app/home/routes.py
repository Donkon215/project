from flask import render_template, jsonify
from app.home import home_bp
import random 

@home_bp.route('/')
@home_bp.route('/home')
def home():
    return render_template('home.html')

