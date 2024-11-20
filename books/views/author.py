from books.models.books import Author
from books.serializers.author import AuthorSerializer
from common.views.mixins import ExtendedGenericViewSet, CRUViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    list=extend_schema(summary='получение всех авторов', tags=[
        'Авторы']),
    create=extend_schema(summary='добавление автора', tags=[
        'Авторы']),
    update=extend_schema(summary='полное обновление автора',
                         tags=['Авторы']),
    destroy=extend_schema(summary='удаление автора',
                          tags=['Авторы']),
    retrieve=extend_schema(summary='получение конкретного автора',
                           tags=['Авторы']),
    partial_update=extend_schema(summary='Частичное обновление автора',
                                 tags=['Авторы']),

)
class AuthorView(CRUViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
