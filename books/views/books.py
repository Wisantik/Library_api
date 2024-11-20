from turtle import update
from venv import create
import books
from books.models.books import Book
from books.serializers.books import BookSerializer
from common.views.mixins import ExtendedGenericViewSet, CRUViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    list=extend_schema(summary='получение всех книг', tags=[
        'Книги']),
    create=extend_schema(summary='добавление книги', tags=[
        'Книги']),
    update=extend_schema(summary='полное обновление книги',
                         tags=['Книги']),
    destroy=extend_schema(summary='удаление книги',
                          tags=['Книги']),
    retrieve=extend_schema(summary='получение конкретной книги',
                           tags=['Книги']),
    partial_update=extend_schema(summary='Частичное обновление книги',
                                 tags=['Книги']),

)
class BookView(CRUViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def get(self, request, *args, **kwargs):
    #     comments = books.comments.get(all)
    #     return comments
