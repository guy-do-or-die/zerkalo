from ..models import Movie, Vote
from .base import AdminModelView


class MovieModelView(AdminModelView):
    __model__ = Movie

    columns_excludei_list = ('url', 'pic')

    column_searchable_list = ('name',)


def _init(admin):
    admin.add_view(
        MovieModelView(
            url='movies',
            name='Movie',
            endpoint='movie',
        )
    )

    admin.add_view(
        AdminModelView(
            Vote,
            url='votes',
            name='Vote',
            endpoint='vote'
        )
    )
