import json
from api import BASE_URL, API_KEY
import requests
from model import Weather, dt


def get_weather(city: str, mock: bool = True) -> dict:
    if mock:
        with open('weather.json', 'r') as f:
            return json.load(f)

    payload = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=payload)
    data: dict = response.json()


    # FOR SAVING MOCK DATA
    # with open('weather.json', 'w') as f:
    #     json.dump(data, f)

    return data


def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get('list')

    if not days:
        raise Exception(f'Problem with Json data')
    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather := day.get('weather')),
                             description=weather[0].get('description')
                             )
        list_of_weather.append(w)

    return list_of_weather
