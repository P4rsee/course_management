from user import user_blue
from flask import Flask, render_template, request, flash, session, jsonify, redirect, url_for, g
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo
from flask_sqlalchemy import SQLAlchemy
from models import User
from models import db



############################# REGISTER #############################

class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('password', 'Inconsistent password input')])
    input = SubmitField('Submit')


@user_blue.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    error = None
    success = None

    if request.method == 'POST':

        if register_form.validate_on_submit():

            username = request.form.get('username')
            password = request.form.get('password')
            password2 = request.form.get('password2')

            user = User.query.filter_by(username=username).first()
            if user:
                error = 'User already exists'
            else:
                user = User(username=username, password = password)
                db.session.add(user)
                db.session.commit()
                success = 'Successful'
                return redirect(url_for('user.login'))

        else:
            error = 'Error'

    return render_template('register.html', form=register_form, error=error, success=success)


########################### LOGIN #############################

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    input = SubmitField('Submit')


@user_blue.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None

    if request.method == 'POST':

        if login_form.validate_on_submit():

            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter_by(username=username, password=password).first()
            if user:
                # Login successful, save user login status
                session['username'] = username
                session['user_id'] = user.id
                g.user = user
                return redirect(url_for('course.index', page=1))
            else:
                # Login failed, return error message to user
                error = 'Incorrect username or password'
        else:
            error = 'Error'

    return render_template('login.html', form=login_form, error=error)

##################### LOGOUT ########################
@user_blue.route('/logout/',methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('user.login'))



