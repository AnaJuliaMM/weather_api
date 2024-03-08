from django.shortcuts import render
from rest_framework import views
from .models import WeatherEntity
from .serializer import TemperatureForecastSerializer
from  django.http import HttpResponse
from random import randrange
from datetime import datetime
from .repository import WeatherRepository



class WeatherView(views.View):        
    def get(request):
        repository = WeatherRepository('aaa')
        weathers = repository.list()
        return render(request, "api/forecasts.html", {"weathers": weathers})

        


class WeatherGenerate(views.View):        
    def get(request):
        weathers = []
        for i in range(10):
            weathers.append(
                WeatherEntity(
                    temperature=randrange(start=17, stop=40),
                    date_time=datetime.now()
                ))
        return render(request, "api/forecasts.html", {"weathers": weathers})

