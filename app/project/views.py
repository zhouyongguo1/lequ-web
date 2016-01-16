from flask import render_template

from . import bp


@bp.route('/')
def index():
    return render_template("project/index.html")


@bp.route('/new')
def add():
    return render_template("project/add.html")


@bp.route('/archived')
def archived():
    return render_template("project/archived.html")


@bp.route('/view')
def view():
    return render_template("project/view.html")
