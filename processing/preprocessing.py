def add_warm_clothes(weather: dict) -> dict:
    weather["warm_clothes"] = weather["temp_c"] < 0
    return weather


def add_expensive(rate: float) -> bool:
    return rate > 100