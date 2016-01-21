from flask import render_template

from lequ.project import bp
from lequ.project.models import Project


@bp.route('/<int:project_id>/tasks')
def task(project_id):
    pro = Project.query.get_or_404(project_id)
    return render_template("project/tasks.html", pro=pro)
