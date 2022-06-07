from flask import Blueprint, render_template
#defines that this file contais the blueprint of all the files

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return  render_template('base.html')