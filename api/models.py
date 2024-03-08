
# Create a generic model
class WeatherEntity:

    def __init__(self, temperature, date_time, atmospheric_pressure='', humidity='', precipitation_percentage='', weather_conditions='',city_name="Sorocaba" ) -> None:
        self.city_name = city_name
        self.temperature = temperature
        self.atmospheric_pressure = atmospheric_pressure
        self.humidity = humidity
        self.precipitation_percentage = precipitation_percentage
        self.weather_conditions = weather_conditions
        self.date_time = date_time

    def __str__(self) -> str:
        return f"Weather Report for {self.city_name}:\n" \
            f"Temperature: {self.temperature} °C\n" \
            f"Atmospheric Pressure: {self.atmospheric_pressure} hPa\n" \
            f"Humidity: {self.humidity}%\n" \
            f"Precipitation Percentage: {self.precipitation_percentage}%\n" \
            f"Weather Conditions: {', '.join(self.weather_conditions)}\n" \
            f"Date and Time: {self.date_time}"