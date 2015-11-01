from ..models import Movie, Vote, Nomination
from .base import AdminModelView


class MovieModelView(AdminModelView):
    __model__ = Movie

    column_exclude_list = ('url', 'pic')
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

    admin.add_view(
        AdminModelView(
            Nomination,
            url='nominations',
            name='Nomination',
            endpoint='Nomination'
        )
    )
