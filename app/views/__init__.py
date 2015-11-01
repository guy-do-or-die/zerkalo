import sys

from flask.ext.admin import Admin

from .base import MainView


def init(app):
    admin = Admin(app,
                  name='Zerkalo',
                  base_template='base.html',
                  template_mode='bootstrap3',
                  index_view=MainView(url='/app',
                                      name='Main',
                                      template='main.html'))

    app.admin_root = admin

    def init_module(name):
        __import__(name)
        module = sys.modules[name]
        try:
            _init = getattr(module, '_init')
        except AttributeError:
            raise Exception('Module {} has no admin_init function'.format(name))
        else:
            _init(admin)

    init_module('app.views.movie')
    init_module('app.views.security')
