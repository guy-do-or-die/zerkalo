from .. import db, SCHEMA


class Movie(db.Model):
    __tablename__ = 'movie'
    __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.Text)
    pic = db.Column(db.Text)
    rate = db.Column(db.Integer)
    status = db.Column(db.Integer)

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
