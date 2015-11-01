from flask import render_template, current_app

from . import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:path>')
def img(path):
    return current_app.send_static_file(path)


@app.errorhandler(403)
def internal_error403(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def internal_error404(error):
    return render_template('404.html'), 404


@app.errorhandler(400)
def internal_error400(error):
    return render_template('400.html'), 400


@app.errorhandler(500)
def internal_error500(error):
    return render_template('500.html'), 500
