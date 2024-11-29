from books.models.books import Book
from books.serializers.commentaries import CommentariesSerializer
from common.serializers.mixins import ExtendedModelSerializer
from rest_framework import serializers


class BookSerializer(ExtendedModelSerializer):
    comments = CommentariesSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['name', 'genres', 'pages', 'author',
                  'comments', 'description', 'date', 'rating']
