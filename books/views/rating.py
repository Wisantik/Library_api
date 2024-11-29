from rest_framework.response import Response
from books.models.books import Book, Rating
from books.serializers.rating import RatingSerializer
from common.views.mixins import ExtendedGenericViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import status


@extend_schema(
    parameters=[OpenApiParameter(
        name="id", type=str, location=OpenApiParameter.PATH), OpenApiParameter(
        name="nested_1_pk", type=str, location=OpenApiParameter.PATH)]
)
class RatingView(ExtendedGenericViewSet):
    def get_serializer_class(self):
        serializer = RatingSerializer
        return serializer

    @extend_schema(summary="Получить список всех оценок для конкретной книги", tags=['Рейтинг у книги'])
    def list(self, request, book_pk=None):
        try:
            book = Book.objects.get(pk=book_pk)
            ratings = book.ratings.all()
            serializer = RatingSerializer(ratings, many=True)
            # book.update_rating()
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(summary="Создать оценку для конкретной книги", tags=['Рейтинг у книги'])
    def create(self, request, book_pk=None):
        try:
            book = Book.objects.get(pk=book_pk)
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(book=book)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        rating_instance = serializer.save()
        # Обновляем рейтинг книги после добавления новой оценки
        book = rating_instance.book
        book.update_rating()

    def perform_update(self, serializer):
        rating_instance = serializer.save()
        # Обновляем рейтинг книги после обновления оценки
        book = rating_instance.book
        book.update_rating()
