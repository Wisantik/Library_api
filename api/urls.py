from django.urls import include, path
from api.spetacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as user_urls
from books.urls import urlpatterns as books_urls
app_name = 'api'

urlpatterns = [
    # path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += user_urls
urlpatterns += books_urls
