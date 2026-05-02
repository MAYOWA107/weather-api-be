import requests

from django.conf import settings


def get_weather_data(city):
    api_key = settings.WEATHER_API_KEY

    url = f"https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(response.text)

        return None

    return response.json()
