import argparse
import json

from processing.service import build_city_summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=True)
    parser.add_argument("--currency", default="USD")
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    try:
        summary = build_city_summary(args.city, args.currency)
        if args.json:
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return
    except ValueError as e:
        print(e)
        raise SystemExit(3)
    except Exception as e:
        print(f"Внешний сервис недоступен: {e}")
        raise SystemExit(4)

    print(f"Город: {summary['city']}")
    print(
        f"Погода: {summary['weather']['temp_c']}°C, "
        f"{summary['weather']['description']}"
    )
    print(
        f"Тёплая одежда: "
        f"{'да' if summary['weather']['warm_clothes'] else 'нет'}"
    )
    print(
        f"{summary['rates']['currency']}→RUB: "
        f"{summary['rates']['rate_to_rub']:.2f}"
    )
    print(
        f"Дорогой курс: "
        f"{'да' if summary['rates']['expensive'] else 'нет'}"
    )


if __name__ == "__main__":
    main()