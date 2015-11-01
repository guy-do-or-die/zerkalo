from .models import Movie
from . import db

from flask import Blueprint, jsonify
import json

module = Blueprint('api', __name__)


@module.route('/api/movies')
def movies():
    ms = db.session.query(Movie).filter(Movie.status > 0).all()
    return json.dumps([o.to_json for o in ms])


@module.route('/api/movie/<int:movie_id>')
def movie(movie_id):
    return jsonify(db.session.query(Movie).get(movie_id).to_json)


@module.route('/api/vote/<int:movie_id>')
def vote(movie_id):
    m = db.session.query(Movie).get(movie_id)
    m.rate += 1

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
            'created_at': 'n/a'
        } for o in ms]
    })
