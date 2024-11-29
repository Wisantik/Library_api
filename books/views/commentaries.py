from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from books import serializers
from books.models.books import Book, comment
from books.models import books
from books.serializers.commentaries import CommentariesSerializer
from books.models.books import comment
from books.serializers.commentaries import CommentariesSerializer
from common.views.mixins import CRUDViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes


@extend_schema(
    parameters=[OpenApiParameter(
        name="id", type=str, location=OpenApiParameter.PATH)]
)
class CommentViewSet(CRUDViewSet):

    def get_serializer_class(self):
        serializer = CommentariesSerializer
        return serializer

    @extend_schema(summary="Получить список всех комментариев для конкретной книги", tags=['Комментарии у книги'])
    def list(self, request, book_pk=None):

        try:
            book = Book.objects.get(pk=book_pk)
            comments = book.comments.all()
            serializer = CommentariesSerializer(comments, many=True)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(summary="Создать комментарий для конкретной книги", tags=['Комментарии у книги'])
    def create(self, request, book_pk=None):
        try:
            book = Book.objects.get(pk=book_pk)
            serializer = CommentariesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(book=book)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(summary="Получить конкретный комментарий по id у конкретной книги", tags=['Комментарии у книги'])
    def retrieve(self, request, pk=None, book_pk=None):
        try:
            book = Book.objects.get(pk=book_pk)
            comment = book.comments.get(pk=pk)
            serializer = CommentariesSerializer(comment)
            return Response(serializer.data)
        except (Book.DoesNotExist,):
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(summary="Обновить комментарий по id у конкретной книги", tags=['Комментарии у книги'])
    def update(self, request, pk=None, book_pk=None):
        try:
            book = Book.objects.get(pk=book_pk)
            comment = book.comments.get(pk=pk)
            serializer = CommentariesSerializer(
                comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (Book.DoesNotExist,):
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(summary="Удалить комментарий по id у конкретной книги", tags=['Комментарии у книги'])
    def destroy(self, request, pk=None, book_pk=None):
        try:
            book = Book.objects.get(pk=book_pk)
            comment = book.comments.get(pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except (Book.DoesNotExist,):
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
