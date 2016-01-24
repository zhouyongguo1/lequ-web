from flask import render_template
from flask.ext.login import login_required

from lequ import db, app
from lequ.core.models import User


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = User.query.filter_by(id=1).first()

    return render_template("home.html", user=user)


@app.route('/teams')
def teams():
    user = User.query.filter_by(id=1).first()
    return render_template("home.html", user=user)


@app.route('/events')
def events():
    return render_template("events.html")


@app.route('/roles')
def roles():
    return render_template("roles.html")
