# from flask_debugtoolbar import DebugToolbarExtension
import sys
import os.path

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

ROOT = os.path.dirname(os.path.dirname(__file__))

app = Flask(__name__, static_folder='static')

app.config.from_object('settings')
app.config.from_envvar('LOCAL_SETTINGS', silent=True)

db = SQLAlchemy(app)

SCHEMA = app.config['SCHEMA']


def init_module(name, mname='module', iname='init'):
    __import__(name)
    module = sys.modules[name]
    if hasattr(module, mname):
        app.register_blueprint(getattr(module, mname))

    if hasattr(module, iname):
        getattr(module, iname)(app)


with app.app_context():
    init_module('app.views')
    init_module('app.routes')
    init_module('app.auth')
    init_module('app.api')


    @app.teardown_appcontext
    def shutdown_session(response):
        db.session.remove()
