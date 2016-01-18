import os
import sys

import pymysql
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

sys.path.append(os.path.dirname(__file__))

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('config.default')
# app.config.from_envvar('APP_CONFIG_FILE')
# app.config.from_envvar('config')
db = SQLAlchemy(app)


def register_blueprints(app):
    from lequ.project import bp as project_bp
    from lequ.work import bp as work_bp
    app.register_blueprint(work_bp, url_prefix='/team/<team_id>/works')
    app.register_blueprint(project_bp, url_prefix='/team/<team_id>/project')


register_blueprints(app)
from lequ import views
