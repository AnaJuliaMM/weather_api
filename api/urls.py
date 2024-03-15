from django.contrib import admin
from django.urls import path, include
from .views import WeatherView


urlpatterns = [
    path('', WeatherView.login, name="login"),
    path('forecasts', WeatherView.get, name="forecasts"),
    path('forecasts/forecast', WeatherView.post_forecast, name="post_forecast"),
    # path('generate', WeatherGenerate.get, name="generate")

]
