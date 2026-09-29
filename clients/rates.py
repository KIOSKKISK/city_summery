import requests

from clients.http import get


def get_rate(currency: str) -> float:
    url = f"https://api.frankfurter.dev/v2/rate/{currency}/RUB"

    try:
        response = get(url)
    except requests.exceptions.HTTPError:
        raise ValueError("Валюта не найдена")

    try:
        data = response.json()
    except ValueError:
        raise RuntimeError("Сервис валют вернул некорректный JSON")

    if not isinstance(data, dict):
        raise RuntimeError("Некорректный ответ сервиса валют")

    if "rate" not in data:
        raise RuntimeError("В ответе сервиса валют отсутствует курс")

    rate = data["rate"]

    if not isinstance(rate, (int, float)) or isinstance(rate, bool):
        raise RuntimeError("Некорректное значение курса")

    return float(rate)