from django.urls import path, include

urlpatterns = [
    path('api/', include('Forecast.urls.api_urls', namespace='api'))
]