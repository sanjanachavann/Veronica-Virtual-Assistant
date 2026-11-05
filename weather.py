
import os
import requests
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("WEATHER_API_KEY")

api_address = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q=Belgaum&appid={key}"
)

json_data = requests.get(api_address).json()
print("Weather API response:", json_data)

def temp():
    temperature = round(json_data["main"]["temp"] - 273, 1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description
