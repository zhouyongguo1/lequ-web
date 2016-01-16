import pymysql
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from .work import bp as work
from .project import bp as project

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.register_blueprint(work, url_prefix='/works')
app.register_blueprint(project, url_prefix='/project')
app.config.from_object('config.default')
# app.config.from_envvar('APP_CONFIG_FILE')
# app.config.from_envvar('config')
db = SQLAlchemy(app)

from app import views
