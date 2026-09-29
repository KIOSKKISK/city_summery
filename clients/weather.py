from clients.http import get


def get_weather(city: str) -> dict:
    # Получаем координаты города
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    response = get(url, params=params)

    # Проверяем корректность JSON геокодера
    try:
        data = response.json()
    except ValueError:
        raise RuntimeError("Геокодер вернул некорректный JSON")

    if not isinstance(data, dict):
        raise RuntimeError("Некорректный ответ геокодера")

    results = data.get("results")

    if results is None or results == []:
        raise ValueError("Город не найден")

    if not isinstance(results, list):
        raise RuntimeError("Некорректный формат результатов геокодера")

    result = results[0]

    if not isinstance(result, dict):
        raise RuntimeError("Некорректные данные города")

    latitude = result.get("latitude")
    longitude = result.get("longitude")

    if (
        not isinstance(latitude, (int, float))
        or isinstance(latitude, bool)
        or not -90 <= latitude <= 90
    ):
        raise RuntimeError("Некорректная широта города")

    if (
        not isinstance(longitude, (int, float))
        or isinstance(longitude, bool)
        or not -180 <= longitude <= 180
    ):
        raise RuntimeError("Некорректная долгота города")

    # Получаем текущую погоду
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",
    }

    response = get(weather_url, params=weather_params)

    # Проверяем корректность JSON погоды
    try:
        weather_data = response.json()
    except ValueError:
        raise RuntimeError("Сервис погоды вернул некорректный JSON")

    if not isinstance(weather_data, dict):
        raise RuntimeError("Некорректный ответ сервиса погоды")

    current = weather_data.get("current")

    if not isinstance(current, dict):
        raise RuntimeError("В ответе погоды отсутствует поле current")

    temperature = current.get("temperature_2m")
    weather_code = current.get("weather_code")

    if (
        not isinstance(temperature, (int, float))
        or isinstance(temperature, bool)
    ):
        raise RuntimeError("Некорректная температура")

    if (
        not isinstance(weather_code, int)
        or isinstance(weather_code, bool)
    ):
        raise RuntimeError("Некорректный код погоды")

    # Переводим код погоды в текстовое описание
    descriptions = {
        0: "clear sky",
        1: "mainly clear",
        2: "partly cloudy",
        3: "overcast",
        45: "fog",
        48: "depositing rime fog",
        51: "light drizzle",
        53: "moderate drizzle",
        55: "dense drizzle",
        61: "rain",
        63: "moderate rain",
        65: "heavy rain",
        71: "snow",
        73: "moderate snow",
        75: "heavy snow",
        80: "rain showers",
        81: "moderate rain showers",
        82: "violent rain showers",
        95: "thunderstorm",
        96: "thunderstorm with hail",
        99: "heavy thunderstorm with hail",
    }

    return {
        "temp_c": temperature,
        "description": descriptions.get(
            weather_code,
            "unknown weather",
        ),
    }