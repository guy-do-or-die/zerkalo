from .models import Movie, Vote
from . import db

from functools import wraps

from flask import Blueprint, jsonify
from flask.ext.security import current_user
import json

module = Blueprint('api', __name__)


def add_headers(headers):
    def pre_inner(func):
        @wraps(func)
        def inner(*args, **kwargs):
            r = func(*args, **kwargs)
            print type(r), r
            for header in headers:
                r.headers[header[0]] = header[1]
            return r
        return inner
    return pre_inner


@module.route('/api/movies')
def movies():
    ms = db.session.query(Movie).filter(Movie.status > 1).all()
    return json.dumps([o.to_json for o in ms])


@module.route('/api/shortlist')
def shortliist():
    ms = db.session.query(Movie).filter(Movie.status > 2).all()
    return json.dumps([o.to_json for o in ms])


@module.route('/api/personal')
def perosnal():
    if current_user.is_anonymous():
        return []
    else:
        ms = db.session.query(Movie).filter(Movie.user_id == current_user.id).all()
        return json.dumps([o.to_json for o in ms])


@module.route('/api/movie/<int:movie_id>')
def movie(movie_id):
    return jsonify(db.session.query(Movie).get(movie_id).to_json)


@module.route('/api/vote/<int:movie_id>')
def vote(movie_id):
    m = db.session.query(Movie).get(movie_id)
    m.rate += 1

    db.session.add(Vote(movie_id, getattr(current_user, 'id', None)))

    try:
        db.session.commit()
        return jsonify({'ok': m.rate})
    except:
        pass

    return jsonify({'error': ''})


@module.route('/api/timeline.json')
def timeline():
    ms = db.session.query(Movie).filter(Movie.status > 0).all()
    return json.dumps({
        'err_code': 0,
        'err_msg': 'success',
        'data': [{
            'id': o.id,
            'title': o.name,
            'nickname': 'Balzac',
            'avatar': '5',
            'text': o.description,
            'original_pic': o.pic,
            'iframe': o.url,
            'created_at': 'n/a',
            'rate': o.rate,
            'user_id': o.rate
        } for o in ms]
    })
