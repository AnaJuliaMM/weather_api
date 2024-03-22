from django import forms

class WeatherForm(forms.Form):
    city_name = forms.CharField(required=False)
    temperature = forms.FloatField()
    atmospheric_pressure = forms.FloatField(required=False)
    humidity = forms.FloatField(required=False)
    precipitation_percentage = forms.FloatField(required=False)
    weather_conditions = forms.CharField(required=False)
    date_time = forms.DateTimeField(required=False)

