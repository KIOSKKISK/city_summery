import time

import requests


def get(url: str, params: dict | None = None) -> requests.Response:
    for attempt in range(3):
        try:
            response = requests.get(
                url,
                params=params,
                timeout=10,
            )

            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")

                if retry_after and retry_after.isdigit():
                    time.sleep(int(retry_after))
                    continue

                raise requests.exceptions.RequestException(
                    "Слишком много запросов"
                )

            if response.status_code in (500, 502, 503, 504):
                if attempt < 2:
                    time.sleep(1)
                    continue

            response.raise_for_status()
            return response

        except (
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
        ):
            if attempt == 2:
                raise

            time.sleep(1)

    raise requests.exceptions.RequestException("Сервис недоступен")