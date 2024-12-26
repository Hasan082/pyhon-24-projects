from weather_api import get_weather, get_weather_details, Weather
import logging


def main():
    while True:
        weather_place = input('Enter city name or postal code: ')
        try:
            current_weather: dict = get_weather(city=weather_place, mock=False)
            status_code = current_weather.get('cod', 0)
            print(f"City form api:  {current_weather.get('city').get('name')}")
            print(f'Current weather status: {status_code}')
            if status_code == str(200):
                break
            elif status_code == str(404):
                print(f'You put wrong city name \'{weather_place}\'. Please try with correct city name')
            elif status_code == str(401):
                print("Unauthorized Access")
            else:
                print(f'Something went wrong. Please try again')

        except ValueError as error:
            logging.error(error)
        except Exception as error:
            logging.error(error)

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
