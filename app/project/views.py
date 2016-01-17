from flask import render_template, redirect, url_for, request

from app.project.form import ProjectForm
from app.project.models import Task
from . import bp


@bp.route('/')
def index():
    pro = Task()
    return render_template("project/index.html")


@bp.route('/new', methods=['GET'])
def add():
    return render_template("project/add.html")


@bp.route('/new', methods=['POST'])
def create():
    form = ProjectForm(request.form)
    if form.validate():
        return redirect(url_for('add'))
    return redirect('team/1/project/1/tasks')


@bp.route('/archived')
def archived():
    return render_template("project/archived.html")


@bp.route('/view')
def view():
    return render_template("project/view.html")
