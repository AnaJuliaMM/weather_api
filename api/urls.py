from django.contrib import admin
from django.urls import path, include
from .views import WeatherView, WeatherInsert


urlpatterns = [
    path('', WeatherView.login, name="login"),
    path('forecasts/', WeatherView.list, name="forecasts"),
    path('forecasts/forecast/', WeatherInsert.as_view(), name="post_forecast"),
    path('forecasts/insert/', WeatherView.post, name="insert_forecast"),
    path('forecasts/forecast/<str:document_id>/', WeatherView.getById, name="forecast"),
    path('forecasts/<str:attribute>/<str:value>/', WeatherView.filterByAttribute, name="filter"),
    path('forecasts/forecast/<str:document_id>/delete', WeatherView.delete, name="delete_by_id"),
    path('forecasts/delete/', WeatherView.deleteAll, name="delete_all"),


]
