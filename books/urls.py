from rest_framework.routers import DefaultRouter
from django.urls import path, include

from rest_framework_nested import routers
from books.models.books import Rating, comment
from books.views.commentaries import CommentViewSet
from books.views.books import BookView
from books.views.author import AuthorView
from books.views.genres import GenreView
from books.views.rating import RatingView

router = routers.DefaultRouter()
router.register(r'books', BookView)
router.register(r'author', AuthorView)
router.register(r'genre', GenreView)
router.register(r'ratings', RatingView, basename='ratings')
urlpatterns = router.urls

nested_router = routers.NestedDefaultRouter(
    router, r'ratings', lookup='book')
nested_router.register(r'ratings', RatingView, basename='ratings')

# Для комментариев создайте вложенные маршруты
comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'update',  # Для частичного обновления
    'delete': 'destroy'
})
ratings_list = RatingView.as_view({
    'get': 'list',
    'post': 'create',
    # 'patch': 'update',
})


urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(nested_router.urls)),
    path('books/<int:book_pk>/comments/',
         comments_list, name='book-comments-list'),
    path('books/<int:book_pk>/comments/<int:pk>/',
         comments_detail, name='book-comment-detail'),
    path('books/<int:book_pk>/ratings/', ratings_list, name='book-ratings-list')
]
