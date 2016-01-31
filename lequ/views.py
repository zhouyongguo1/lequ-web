from flask import render_template, flash, request
from flask.ext.login import login_required, current_user

from lequ import db, app
from lequ.core.models import User, UserTeam
from lequ.core.services import create_team


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


@app.route('/team/<int:team_id>')
@login_required
def team_home(team_id):
    user = User.query.filter_by(id=1).first()
    return render_template("home.html", user=user)


@app.route('/teams', methods=["GET"])
def teams():
    user_teams = UserTeam.query.filter_by(user_id=current_user.id).all()
    return render_template("teams.html", user_teams=user_teams)


@app.route('/teams/new', methods=["POST"])
def new_team():
    team_name = request.form['name']
    create_team(team_name, current_user)
    user_teams = UserTeam.query.filter_by(user_id=current_user.id).all()
    flash('新建团队成功')
    return render_template("teams.html", user_teams=user_teams)


@app.route('/events')
def events():
    return render_template("events.html")


@app.route('/roles')
def roles():
    return render_template("roles.html")
