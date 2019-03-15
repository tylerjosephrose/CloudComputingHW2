from django.urls import path, re_path
from .api.api import HistoricalListApi, HistoricalLookupApi


urlpatterns = [
    path('historical/', HistoricalListApi.as_view(), name="historical"),
    re_path(r'^historical/(?P<date>\d{4}\d{2}\d{2})$', HistoricalLookupApi.as_view(), name='historicalLookup'),
]