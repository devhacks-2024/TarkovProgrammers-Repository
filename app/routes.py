from flask import url_for, render_template, request, redirect, flash, app_route, abort
from flask_wtf import FlaskForm
from flask_wtf import StringField, PasswordField, validators, url_has_allowed_host_and_scheme
from flask_login import login_user
from mainappmodule import app
from models import User

class LoginForm(FlaskForm):
    username = StringField('username', [validators.required()])
    password = PasswordField('password', [validators.required()])

@app_route('/')
def index():
    return render_template('index.html')

@app_route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        cur_user = User(username = form.username.data)
        cur_user.password(form.password.data)
        login_user(cur_user)
        flash('Logged in successfully.')
        next = request.args.get('next')
        if not url_has_allowed_host_and_scheme(next, request.host):
            return abort(400)
        return redirect(next or url_for('index'))
    return render_template('login.html', form=form)

@app_route('/register')
def register():

    return render_template('register.html')