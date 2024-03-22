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
        try:
            repository = WeatherRepository('forecasts')
            # Transform Cursor object in a list of documents
            documents = list(repository.list()) 
            # Serializer: validate fields
            serializer = WeatherSerializer(data=documents, many=True)
            if serializer.is_valid():
                # Serializer: transform from json to object
                weathers = serializer.save()
                return render(request, "api/forecasts.html", {"weathers": weathers})
            else: 
                return render(request, "api/forecasts.html", {"error" : serializer.errors})
        except ValueError as e:
            return render(request, "api/forecasts.html", {"error" : e})
        except Exception as e:
            return render(request, "api/forecasts.html", {"error" : e})
            
    
    def getById(request, document_id):
        try:
            repository = WeatherRepository('forecasts')
            documents = list(repository.getById(document_id))
            serializer = WeatherSerializer(data=documents, many=True)
            if serializer.is_valid():
                weather = serializer.save()
                return render(request, "api/forecasts.html", {"weathers": weather})
            else: 
                return render(request, "api/forecasts.html", {"error" : serializer.errors})
        except ValueError as e:
            return render(request, "api/forecasts.html", {"error" : e})
        except Exception as e:
            return render(request, "api/forecasts.html", {"error" : e})
    
    def filterByAttribute(request, attribute, value):
        try:
            repository = WeatherRepository('forecasts')
            documents = list(repository.filterByAttribute(attribute, value))
            serializer = WeatherSerializer(data=documents, many=True)
            if serializer.is_valid():
                weather = serializer.save()
                return render(request, "api/forecasts.html", {"weathers": weather})
            else: 
                return render(request, "api/forecasts.html", {"error" : serializer.errors})
        except ValueError as e:
            return render(request, "api/forecasts.html", {"error" : e})
        except Exception as e:
            return render(request, "api/forecasts.html", {"error" : e})

    def post(request):
        try:
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
        except ValueError as e:
            return render(request, "api/forecasts.html", {"error" : e})
        except Exception as e:
            return render(request, "api/forecasts.html", {"error" : e})
    
    def delete(request, document_id):
        repository = WeatherRepository('forecasts')
        repository.delete(document_id)
        return render(request, "api/forecasts.html")

    def deleteAll(request):
        repository = WeatherRepository('forecasts')
        repository.deleteAll()
        return render(request, "api/forecasts.html")
    
class WeatherTemplateView(View):
    def post_forecast_template(request):
        return render(request, "api/post_forecast.html")
   

