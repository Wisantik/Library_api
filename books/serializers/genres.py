from books.models.books import Genre
from common.serializers.mixins import ExtendedModelSerializer
from rest_framework import serializers


class GenreSerializer(ExtendedModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
