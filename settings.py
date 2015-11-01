import os

HOST = '0.0.0.0'
PORT = 5000
SECRET_KEY = 'guess'
CSRF_ENABLED = True

DEBUG = True
SQL_ECHO = True

SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_POOL_RECYCLE = 300

# SQLALCHEMY_DATABASE_URI = 'postgresql://zerkalo:zerkalo@localhost/zerkalo'
SQLALCHEMY_DATABASE_URI = 'postgresql://ldjlupbwgtvcmh:cFo8y5RR2bYcnpvoUdjMDg6sJa@ec2-54-217-202-110.eu-west-1.compute.amazonaws.com/d802g2ejv7g9tb'

SQLALCHEMY_TRACK_MODIFICATIONS = False

SCHEMA = 'public'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'app/static/img')
MEDIA_URL = '/static/'

GOOGLE_ACCOUNTS_BASE_URL = 'https://accounts.google.com'
GOOGLE_ACCESS_SCOPE = 'email'
GOOGLE_ACCESS_TOKEN_URL = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token='
GOOGLE_CLIENT_ID = '552795822287-h5le6mp6ar6l0riplpiqhhliqhb797ut.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'rgwIPxf1FBbtF6DmHwOegxNQ'
# REDIRECT_URI = 'http://localhost:5000/oauth2callback'
REDIRECT_URI = 'http://zerkalo.herokuapp.com/oauth2callback'
