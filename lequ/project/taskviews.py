from flask import render_template

from lequ.project import bp


@bp.route('/archived')
def task():
    return render_template("project/archived.html")

