from flask.ext.security import UserMixin

from .. import db, SCHEMA

import json


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey(SCHEMA + '.user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey(SCHEMA + '.role.id')),
                       schema=SCHEMA, info={'bind_key': 'main'})


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)

    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    @property
    def permissions(self):
        ps = {}
        for r in self.roles:
            if r.permissions:
                pdict = json.loads(r.permissions)

                for v in pdict:
                    permissions = pdict.get(v, [])

                    if v in ps:
                        ps[v] = list(set(ps[v] + permissions))
                    else:
                        ps[v] = permissions

        return ps

    def is_allowed(self, view, permission):
        vp = self.permissions.get(view)
        return self.is_admin or vp and (permission in vp or 'all' in vp)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __repr__(self):
        return self.email
