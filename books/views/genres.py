
from books.models.books import Genre
from books.serializers.genres import GenreSerializer
from common.views.mixins import ExtendedGenericViewSet, CRUViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    list=extend_schema(summary='получение всех женров', tags=[
        'Жанры']),
    create=extend_schema(summary='добавление жанра', tags=[
        'Жанры']),
    update=extend_schema(summary='полное обновление жанра',
                         tags=['Жанры']),
    destroy=extend_schema(summary='удаление жанра',
                          tags=['Жанры']),
    retrieve=extend_schema(summary='получение конкретной жанра',
                           tags=['Жанры']),
    partial_update=extend_schema(summary='Частичное обновление жанра',
                                 tags=['Жанры']),

)
class GenreView(CRUViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
