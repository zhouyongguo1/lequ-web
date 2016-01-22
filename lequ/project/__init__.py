from flask import Blueprint, g

bp = Blueprint(
    'project',
    __name__,
    template_folder='templates'
)


@bp.url_value_preprocessor
def get_profile_owner(endpoint, values):
    g.team_id = values.pop('team_id')


@bp.url_defaults
def add_user_url_slug(endpoint, values):
    values.setdefault('team_id', g.team_id)


from . import views
from . import taskviews
