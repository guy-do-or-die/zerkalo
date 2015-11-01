from flask.ext.security import RoleMixin

from .. import db, SCHEMA

import json


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    permissions = db.Column('permissions', db.Text)

    @property
    def permissions_dict(self):
        return json.loads(self.permissions) if self.permissions else ''

    def __repr__(self):
        return self.name
