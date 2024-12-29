from weather_api import get_weather, get_weather_details, Weather
import logging


def main():
    while True:
        weather_place = input('Enter city name: ')

        if weather_place.isdigit():
            print("Invalid city name, Please try again!")
            continue

        try:
            current_weather: dict = get_weather(city=weather_place, mock=False)

            if not current_weather or not isinstance(current_weather, dict):
                print("Invalid response from the weather API. Please try again.")
                continue

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
        except ValueError as e:
            print(f"Invalid city name, Please try again!")
            logging.basicConfig(filename='app.log', level=logging.ERROR)
        except Exception as error:
            print(f"Exception Invalid city name, Please try again!")
            logging.basicConfig(filename='app.log', level=logging.ERROR)

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
