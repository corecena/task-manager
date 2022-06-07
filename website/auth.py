

from flask import Blueprint, render_template, redirect, request, flash
#defines that this file contais the blueprint of all the files

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return  render_template('login.html')
    
@auth.route('/logout')
def logout():
    return  redirect('/')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        Email = request.form.get('email')
        FirstName  = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(Email)<4 :
            flash('Email must be greatere than 3 characters', category='error')
        elif len(FirstName)<2:
            flash("First name should be greater than 1 characters" , category='error')
        elif len(password1 != password2):
            flash('Passwords dont match', category='error')
        elif len(password1)< 6:
            flash('Passwords must be 6 charcaters or more', category='error')
        else:
            flash("ACCOUNT created successfully", category='success')
    return  render_template('sign_up.html')