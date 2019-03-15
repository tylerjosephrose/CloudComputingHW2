from rest_framework import serializers
from .models import Weather


class HistoricalSerializer(serializers.ModelSerializer):
    DATE = serializers.DateField(format="%Y%m%d")

    class Meta:
        model = Weather
        fields = ("DATE",)


class HistoricalLookupSerializer(serializers.ModelSerializer):
    DATE = serializers.DateField(format="%Y%m%d")

    class Meta:
        model = Weather
        fields = ("DATE", "TMAX", "TMIN")
