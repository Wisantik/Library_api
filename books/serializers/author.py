from books.models.books import Author
from common.serializers.mixins import ExtendedModelSerializer
from rest_framework import serializers


class AuthorSerializer(ExtendedModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
