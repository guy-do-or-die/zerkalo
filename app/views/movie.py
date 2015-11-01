from ..models import Movie
from .base import AdminModelView


class MovieModelView(AdminModelView):
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
