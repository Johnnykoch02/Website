from os import error
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if  request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully.',category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, try again.', category='error') 
        else:
            flash('This email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return  redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        error = []
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email already exists.', category='error')
            error.append('email_taken')
        if len(email) < 4:
            flash('This is not a valid email!', category='error')
            error.append("email_length")
        
        if len(firstName) < 2:
            flash('This is not a valid Name!', category='error')
            error.append("firstName_length")
       
        if password1 != password2:
            flash('The entered passwords do not match!', category='error')
            error.append("password_match")
      
        elif len(password1) < 7:
            flash('Please create a password with at least 7 Characters!', category='error')
            error.append("password_length")
        print(error)
        if len(error) == 0:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            login_user(new_user, remember=True)
    
            return redirect(url_for('views.home'))
        
    return render_template("sign_up.html", user=current_user)