from weather_api import get_weather, get_weather_details, Weather


def main():
    weather_place = input('Enter city name: ')
    current_weather: dict = get_weather(city=weather_place, mock=False)
    weather_details = get_weather_details(current_weather)

    dfmt: str = '%Y-%m-%d'
    days: list[str] = list(f'{date.date:{dfmt}}' for date in weather_details)

    for day in days:
        print(day)
        print('-' * 6)
        grouped_weather_by_date: list[Weather] = [current for current in weather_details if f'{current.date:{dfmt}}'
                                                  == day]
        for single_group in grouped_weather_by_date:
            print(single_group)

        print('-' * 6)


if __name__ == '__main__':
    main()
