from .models import Movie, Vote
from . import db
from flask import make_response
from flask import Blueprint, jsonify
from flask.ext.security import current_user
import json

module = Blueprint('api', __name__)


@module.route('/api/movies')
def movies():
    ms = db.session.query(Movie).filter(Movie.status > 0).all()
    return json.dumps([o.to_json for o in ms])


@module.route('/api/shortlist')
def shortliist():
    ms = db.session.query(Movie).filter(Movie.status > 1).all()
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
    data = json.dumps({
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

    resp = make_response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp
