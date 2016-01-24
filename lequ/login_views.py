from flask import g, render_template, redirect, url_for, flash
from flask.ext.login import current_user, login_user, logout_user

from lequ.core.models import User
from lequ.forms import LoginForm
from . import app, login_manager


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=["GET"])
def login():
    logout_user()
    return render_template('login.html', form=LoginForm())


@app.route('/login', methods=["POST"])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    flash('用户名或密码错误')
    return render_template('login.html', form=form)
