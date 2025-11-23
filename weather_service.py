import random
import time

class WeatherService:
    def __init__(self):
        # In the future, we can add an API key here for OpenWeatherMap
        self.api_key = None

    def get_weather(self, location):
        """
        Fetches weather data for a specific location.
        Currently uses mock data for testing purposes.
        """
        # simulating network delay to make it feel like a real request
        print(f"... connecting to weather server for {location} ...")
        time.sleep(1.5) 
        
        try:
            # Generating realistic ranges for farming contexts
            # Temp in Celsius, Humidity in %, Rain as boolean
            data = {
                "temp": random.randint(10, 40),
                "humidity": random.randint(30, 95),
                "rain_forecast": random.choice([True, False, False]) # Lower chance of rain
            }
            return data
        except Exception as e:
            print(f"Error: Something went wrong while fetching data. {e}")
            return None