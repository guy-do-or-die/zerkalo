from flask import current_app

from ..models import User, Role
from .base import AdminModelView


class UserModelView(AdminModelView):
    column_list = ('email', 'active', 'is_admin', 'roles')
    column_default_sort = ('email', False)

    column_searchable_list = ('email',)


class RolesModelView(AdminModelView):
    column_default_sort = ('name', False)
    column_exclude_list = ('permissions',)

    column_searchable_list = ('name',)

    def get_views(self):
        views = {}
        for view in current_app.admin_root._views:
            if view.endpoint == 'admin':
                continue
            views.setdefault(view.category, []).append({
                'id': view.endpoint,
                'name': view.name,
                'perms': view.permissions,
            })

        return views


def _init(admin):
    admin.add_view(
        UserModelView(
            User,
            category='Security',
            url='users',
            name='User',
            endpoint='user',
        )
    )

    admin.add_view(
        RolesModelView(
            Role,
            category='Security',
            url='roles',
            name='Role',
        )
    )
