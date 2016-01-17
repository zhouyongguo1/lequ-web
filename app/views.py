from flask import render_template

from app import db, lq
from app.core.models import User


@lq.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@lq.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@lq.route('/')
@lq.route('/index')
def index():
    user = User.query.filter_by(id=1).first()

    return render_template("home.html", user=user)


@lq.route('/events')
def events():
    return render_template("events.html")


@lq.route('/roles')
def roles():
    return render_template("roles.html")
