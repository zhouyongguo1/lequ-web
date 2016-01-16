from flask import render_template

from app import app, db


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/')
@app.route('/index')
def index():
    # user = User()
    # db.session.add(user)
    # db.session.commit()
    # user = User.query.filter_by(id=1).first()

    return render_template("home.html")


@app.route('/events')
def events():
    return render_template("events.html")


@app.route('/roles')
def roles():
    return render_template("roles.html")
