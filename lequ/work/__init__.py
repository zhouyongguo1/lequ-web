from flask import Blueprint, g

bp = Blueprint(
    'work',
    __name__,
    template_folder='templates',
    static_folder='static'
)


from . import views
