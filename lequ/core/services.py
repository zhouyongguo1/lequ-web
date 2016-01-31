from flask.ext.login import current_user

from lequ import db
from lequ.core.models import Team, UserTeam


def create_team(team_name, user):
    team = Team(team_name, current_user.id)
    user_team = UserTeam(team, user, None, True, current_user.id)
    db.session.add(team)
    db.session.add(user_team)
    db.session.commit()
