from flask import render_template, redirect, url_for, request, g

from lequ import db
from lequ.project.form import ProjectForm
from . import bp


@bp.route('/')
def index():
    return render_template("project/index.html")


@bp.route('/new', methods=['GET'])
def add():
    return render_template("project/add.html")


@bp.route('/new', methods=['POST'])
def create():
    form = ProjectForm(request.form)
    if form.validate():
        project = form.to_project()
        db.session.add(project)
        db.session.commit()
        url = '/team/%s/project/%d/tasks' % (g.teamId, project.id)
        return redirect(url)
    else:
        return redirect(url_for('project.add'))


@bp.route('/archived')
def archived():
    return render_template("project/archived.html")


@bp.route('/view')
def view():
    return render_template("project/view.html")
