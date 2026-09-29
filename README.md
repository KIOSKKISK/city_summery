# Сводка по городу

CLI-утилита на Python, которая получает информацию о погоде и курс выбранной валюты к рублю.

## Возможности

- получение города и координат через Open-Meteo;
- получение текущей погоды;
- получение курса валюты к RUB через Frankfurter;
- определение необходимости тёплой одежды;
- определение дорогого курса;
- повторные запросы при временных ошибках;
- обработка ошибок города и валюты;
- JSON-вывод.

## Установка

```bash
py -m pip install -r requirements.txt
## Запуск

Обычный запуск:

```bash
py main.py --city Moscow
py main.py --city Moscow --currency EUR
py main.py --city Moscow --json
py -m pytest
city_summary/
├── main.py
├── requirements.txt
├── README.md
├── clients/
│   ├── http.py
│   ├── weather.py
│   └── rates.py
├── processing/
│   ├── preprocessing.py
│   └── service.py
└── tests/
    └── test_preprocessing.py