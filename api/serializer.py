from rest_framework import serializers
from .models import WeatherEntity

class TemperatureForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherEntity
        fields = '__all__'
