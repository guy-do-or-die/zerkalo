from .. import db, SCHEMA

from datetime import datetime


class Movie(db.Model):
    __tablename__ = 'movie'
    __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    url = db.Column(db.Text)
    pic = db.Column(db.Text)
    rate = db.Column(db.Integer)
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    @property
    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'url': self.url,
            'rate': self.rate
        }

    def __repr__(self):
        return self.name


class Vote(db.Model):
    __tablename__ = 'vote'
    __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    def __init__(self, movie_id, user_id=None, weight=None):
        super(Vote, self).__init__()
        self.date = datetime.now()
        self.movie_id = movie_id
        self.user_id = user_id
        self.weight = weight

    def __repr__(self):
        return self.name


class Nomination(db.Model):
    __tablename__ = 'nomination'
    __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    movie_name = db.Column(db.String)
    description = db.Column(db.Text)
    url = db.Column(db.Text)
    pic = db.Column(db.Text)

    def __repr__(self):
        return self.name
