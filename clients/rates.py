from clients.http import get
import requests


def get_rate(currency: str) -> float:
    url = f"https://api.frankfurter.dev/v2/rate/{currency}/RUB"

    try:
        response = get(url)
    except requests.exceptions.HTTPError:
        raise ValueError("Валюта не найдена")

    data = response.json()

    return float(data["rate"])