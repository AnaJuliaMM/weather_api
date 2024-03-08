from django.contrib import admin
from django.urls import path, include
from .views import WeatherView
from .views import WeatherGenerate


urlpatterns = [
    path('', WeatherView.get, name="view"),
    path('generate', WeatherGenerate.get, name="generate")

]
