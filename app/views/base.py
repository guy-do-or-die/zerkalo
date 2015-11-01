from flask.ext.security import current_user
from flask.ext.admin import BaseView, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView

from .. import db


class AuthMixin(object):
    def is_accessible(self, endpoint=None):
        view = endpoint or self.endpoint
        return self.__class__ == MainView or current_user and current_user.is_allowed(view, 'view')

    @property
    def can_view(self):
        return current_user and current_user.is_allowed(self.endpoint, 'view')

    @property
    def can_create(self):
        return current_user and current_user.is_allowed(self.endpoint, 'edit')

    @property
    def can_edit(self):
        return current_user and current_user.is_allowed(self.endpoint, 'edit')

    @property
    def can_delete(self):
        return current_user and current_user.is_allowed(self.endpoint, 'delete')


class AdminView(AuthMixin, BaseView):
    def __init__(self, name=None, category=None, endpoint=None, url=None):
        super(AdminView, self).__init__(name, category, endpoint, url)
        self.permissions = ['view']


class TemplateVars(object):
    def __init__(self, view, context):
        self.view = view
        self.tpl = context

    def __getattr__(self, name):
        val = getattr(self.view, name)

        if callable(val):
            val = val(self)

        setattr(self, name, val)
        return val


class MainView(AdminIndexView):
    pass


class AdminModelView(AuthMixin, ModelView):
    def __init__(self, model=None, name=None, category=None, endpoint=None, url=None):
        super(AdminModelView, self).__init__(model or self.__model__, db.session, name, category, endpoint, url)

        permissions = set(('view', 'edit', 'delete'))
        for _, v in vars(self).iteritems():
            try:
                permissions.add(getattr(v, 'perm'))
            except AttributeError:
                pass

        for _, v in vars(self.__class__).iteritems():
            try:
                permissions.add(getattr(v, 'perm'))
            except AttributeError:
                pass

        self.permissions = sorted(permissions)
