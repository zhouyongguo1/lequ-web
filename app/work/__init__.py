from flask import Blueprint, g

bp = Blueprint(
    'work',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@bp.url_value_preprocessor
def get_profile_owner(endpoint, values):
    g.teamId = values.pop('team_id')


from . import views
