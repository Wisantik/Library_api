from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import routers

from books.models.books import comment
from books.views.commentaries import CommentViewSet
from books.views.books import BookView
from books.views.author import AuthorView
from books.views.genres import GenreView

router = routers.DefaultRouter()
router.register(r'books', BookView)
router.register(r'author', AuthorView)
router.register(r'genre', GenreView)
router.register(r'commentaries', CommentViewSet, basename="comment")
urlpatterns = router.urls

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

urlpatterns = [
    path('', include(router.urls)),
    path('books/<int:book_pk>/comments/',
         comments_list, name='book-comments-list'),
    path('books/<int:book_pk>/comments/<int:pk>/',
         comments_detail, name='book-comment-detail'),
]
