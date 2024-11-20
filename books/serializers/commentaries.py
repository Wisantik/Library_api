from books.models.books import comment
from common.serializers.mixins import ExtendedModelSerializer
from rest_framework import serializers


class CommentariesSerializer(ExtendedModelSerializer):

    class Meta:
        model = comment
        fields = ['book', 'text']
