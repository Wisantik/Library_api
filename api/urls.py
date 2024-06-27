from django.urls import include, path
from api.spetacular.urls import urlpatterns as doc_urls


app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls