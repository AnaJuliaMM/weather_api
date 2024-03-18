from django.shortcuts import render
from rest_framework.views import View
from .models import WeatherEntity
from .serializer import TemperatureForecastSerializer
from  django.http import HttpResponse
from random import randrange
from datetime import datetime
from .repositories import WeatherRepository
from .models import WeatherEntity



class WeatherView(View):   
    def login(request):
        return render(request, "api/login.html")
         
    def list(request):
        repository = WeatherRepository('forecasts')
        weathers = repository.list()
        return render(request, "api/forecasts.html", {"weathers": weathers})
    
    def get(request, document_id):
        repository = WeatherRepository('forecasts')
        weathers = repository.getById(document_id)
        return render(request, "api/forecasts.html", {"weathers": weathers})
    
    def post_forecast(request):
        return render(request, "api/post_forecast.html")
    
    
    def create(request):
        return render(request, "api/post_forecast.html")
    


# class WeatherGenerate(views.View):        
#     def get(request):
#         weathers = []
#         for i in range(10):
#             weathers.append(
#                 WeatherEntity(
#                     temperature=randrange(start=17, stop=40),
#                     date_time=datetime.now()
#                 ))
#         return render(request, "api/forecasts.html", {"weathers": weathers})

    
    
   
 