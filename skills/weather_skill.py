import requests
from config import OPENWEATHER_API_KEY

def get_weather(location=None):
    """Gets weather for specified location"""
    if not location:
        return "Please specify a location (e.g., 'weather in London')"
    
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}appid={OPENWEATHER_API_KEY}&q={location}&units=metric"
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            return (f"Weather in {location}: {weather['description']}. "
                   f"Temperature: {main['temp']}°C, Humidity: {main['humidity']}%")
        return "Location not found. Please try again."
    except Exception as e:
        return f"Sorry, I couldn't fetch the weather. Error: {str(e)}"