from clients.weather import get_weather
from clients.rates import get_rate
from processing.preprocessing import add_warm_clothes, add_expensive


def build_city_summary(city: str, currency: str = "USD") -> dict:
    weather = get_weather(city)
    rate = get_rate(currency)

    weather = add_warm_clothes(weather)
    expensive = add_expensive(rate)

    return {
        "city": city,
        "weather": weather,
        "rates": {
            "currency": currency,
            "rate_to_rub": rate,
            "expensive": expensive,
        },
    }