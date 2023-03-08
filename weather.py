import json
from datetime import datetime

import requests

# TODO
#   open_weather_map_api = ТВОЙ ТОЕКН С САЙТА openweathermap.org (НУЖНО ЗАРЕГИСТРИРОВАТЬСЯ)
open_weather_map_api = ''


def get_weather_string(location):
    query = {
        'lang': 'ru',
        'lat': location.latitude,
        'lon': location.longitude,
        'units': 'metric',
        'appid': open_weather_map_api
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?', params=query)
    r = json.loads(response.text)

    now = datetime.today().strftime('%d.%m.%Y %H:%M:%S')
    msg = '{}\n{}\n{}\n\n' \
          'Температура: {}°C\n' \
          'Ощущается как: {}°C\n\n' \
          'Ветер: {} м/с.\n' \
          'Порывы до {} м/с\n\n' \
          'Влажность: {}%\n' \
          'Давление: {} мм.рт.столба\n' \
          'Облачность: {}%\n\n' \
          'Закат: {}' \
        .format(now,
                get_data(r, 'name'),
                get_data(r, 'weather', 0, 'description').capitalize(),
                get_data(r, 'main', 'temp'),
                get_data(r, 'main', 'feels_like'),
                get_data(r, 'wind', 'speed'),
                get_data(r, 'wind', 'gust'),
                get_data(r, 'main', 'humidity'),
                get_data(r, 'main', 'pressure'),
                get_data(r, 'clouds', 'all'),
                datetime.fromtimestamp(int(get_data(r, 'sys', 'sunset')))
                .strftime('%H:%M') if get_data(r, 'sys', 'sunset') != '—' else 'ошибка')
    return msg


def get_data(data, *keys):
    for key in keys:
        if key in data:
            data = data[key]
        else:
            return '—'
    return data
