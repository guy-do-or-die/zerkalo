import json
import requests

from flask import request, redirect, abort, Blueprint, current_app
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user
from flask.ext.security import Security, SQLAlchemyUserDatastore, AnonymousUser

from . import db
from .oauth2 import GeneratePermissionUrl
from .models import User, Role

module = Blueprint('auth', __name__)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)


class Anonymous(AnonymousUser):
    name = u'Anonymous'

    def is_allowed(*args, **kwargs):
        return False


@module.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/')


@module.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/app')

    if request.method == 'GET':
        url = GeneratePermissionUrl(current_app.config['GOOGLE_CLIENT_ID'], request.args.get('email', ''),
                                    redirect_uri=current_app.config['REDIRECT_URI'],
                                    google_account_base_url=current_app.config['GOOGLE_ACCOUNTS_BASE_URL'],
                                    scope=current_app.config['GOOGLE_ACCESS_SCOPE'])
        return redirect(url)


@module.route('/oauth2callback', methods=['GET', 'POST'])
def oauth2callback():
    from app.oauth2 import AuthorizeTokens
    if request.method == 'GET':
        code = request.args.get('code', '')
        useremail = request.args.get('state', '')
        response = AuthorizeTokens(current_app.config['GOOGLE_CLIENT_ID'],
                                   current_app.config['GOOGLE_CLIENT_SECRET'],
                                   code,
                                   redirect_uri=current_app.config['REDIRECT_URI'],
                                   google_account_base_url=current_app.config['GOOGLE_ACCOUNTS_BASE_URL'])

        if 'access_token' in response:
            accesstoken = response['access_token']
            r = requests.get(current_app.config['GOOGLE_ACCESS_TOKEN_URL'] + accesstoken)
            j = json.loads(r.text)

            useremail = j['email']

            if useremail:
                user = user_datastore.get_user(useremail)
                if user:
                    login_user(user, remember='yes')
                else:
                    return abort(403)
        else:
            return abort(403)

    return redirect(request.args.get('next', None) or '/app')


def is_static_route():
    p = request.path
    return any(p.startswith(r) for r in ('/img/', '/js/', '/css/', '/static/'))


def init(app):
    security = Security(app, user_datastore)
    security._state.principal._is_static_route = is_static_route
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.anonymous_user = Anonymous

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return user_datastore.get_user(int(user_id))
        except Exception:
            current_app.logger.exception('Erorr')
            return Anonymous()
