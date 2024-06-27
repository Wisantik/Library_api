from django.urls import path

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [

    path('schema', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),

]
