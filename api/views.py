from rest_framework.views import View
from rest_framework.response import Response
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from .serializer import WeatherSerializer
from .repositories import WeatherRepository
from .models import WeatherEntity
from datetime import datetime


class WeatherView(View):   
    def login(request):
        return render(request, "api/login.html")
         
    def list(request):
        repository = WeatherRepository('forecasts')
        weathers = repository.list()
        return render(request, "api/forecasts.html", {"weathers": weathers})
    
    def getById(request, document_id):
        repository = WeatherRepository('forecasts')
        weathers = repository.getById(document_id)
        return render(request, "api/forecasts.html", {"weathers": weathers})
    
    def filterByAttribute(request, attribute, value):
        repository = WeatherRepository('forecasts')
        weathers = repository.filterByAttribute(attribute, value)
        return render(request, "api/forecasts.html", {"weathers": weathers})

    def post_forecast(request):
        return render(request, "api/post_forecast.html")

    def post(request):
        data = request.POST
        model = WeatherEntity(
            temperature=data['temperature'],
            date_time=datetime.now(),
            atmospheric_pressure=data['atmospheric_pressure'],
            humidity=data['humidity'],
            precipitation_percentage=data['precipitation_percentage'],
            weather_conditions=data['weather_conditions'],
            city_name=data['city_name']
        )
        serializer = WeatherSerializer(data=model.__dict__)
        if serializer.is_valid():
            document = serializer.validated_data
            repository = WeatherRepository('forecasts')
            repository.insert(document)
            return render(request, "api/forecasts.html", {"weathers": [serializer.data]})
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(request, document_id):
        repository = WeatherRepository('forecasts')
        repository.delete(document_id)
        return render(request, "api/forecasts.html")

    def deleteAll(request):
        print('delete')
        repository = WeatherRepository('forecasts')
        repository.deleteAll()
        return render(request, "api/forecasts.html")
    
   