from ..models import Movie
from .base import AdminModelView


class MovieModelView(AdminModelView):
    columns_excludei_list = ('url', 'pic')

    column_searchable_list = ('name',)


def _init(admin):
    admin.add_view(
        MovieModelView(
            Movie,
            url='movies',
            name='Movie',
            endpoint='movie',
        )
    )
