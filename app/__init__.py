import pymysql
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from .project import bp as project_bp
from .work import bp as work_bp

pymysql.install_as_MySQLdb()

lq = Flask(__name__)
lq.register_blueprint(work_bp, url_prefix='/team/<team_id>/works')
lq.register_blueprint(project_bp, url_prefix='/team/<team_id>/project')

lq.config.from_object('config.default')
# app.config.from_envvar('APP_CONFIG_FILE')
# app.config.from_envvar('config')
db = SQLAlchemy(lq)

from app import views
