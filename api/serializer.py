from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    city_name = serializers.CharField(required=False)
    temperature = serializers.FloatField()
    atmospheric_pressure = serializers.FloatField(required=False)
    humidity = serializers.FloatField(required=False)
    precipitation_percentage = serializers.FloatField(required=False)
    weather_conditions = serializers.CharField(required=False)
    date_time = serializers.DateTimeField(required=False)