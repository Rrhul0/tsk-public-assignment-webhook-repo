from flask import Blueprint, render_template

web_app = Blueprint('Web', __name__)

@web_app.route('/')
def index():
    return render_template('index.html')