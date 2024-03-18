from django.contrib import admin
from django.urls import path, include
from .views import WeatherView


urlpatterns = [
    path('', WeatherView.login, name="login"),
    path('forecasts', WeatherView.list, name="forecasts"),
    path('forecasts/forecast/', WeatherView.create, name="post_forecast"),
    path('forecasts/forecast/<str:document_id>/', WeatherView.get, name="forecast"),
    # path('generate', WeatherGenerate.get, name="generate")

]
