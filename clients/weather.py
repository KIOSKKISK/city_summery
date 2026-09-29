from clients.http import get


def get_weather(city: str) -> dict:
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    response = get(url, params=params)
    data = response.json()

    if "results" not in data or not data["results"]:
        raise ValueError("Город не найден")

    result = data["results"][0]

    latitude = result["latitude"]
    longitude = result["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",
    }

    response = get(weather_url, params=weather_params)
    weather_data = response.json()

    weather_code = weather_data["current"]["weather_code"]

    descriptions = {
        0: "clear sky",
        1: "mainly clear",
        2: "partly cloudy",
        3: "overcast",
        45: "fog",
        48: "depositing rime fog",
        51: "light drizzle",
        61: "rain",
        71: "snow",
        80: "rain showers",
        95: "thunderstorm",
    }

    return {
        "temp_c": weather_data["current"]["temperature_2m"],
        "description": descriptions.get(weather_code, "unknown weather"),
    }