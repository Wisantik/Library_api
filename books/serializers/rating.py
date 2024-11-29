from books.models.books import Rating
from common.serializers.mixins import ExtendedModelSerializer


class RatingSerializer(ExtendedModelSerializer):
    class Meta:

        model = Rating
        fields = ['score', 'created_by', 'book']
