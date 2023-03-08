import json
from datetime import datetime
import requests

open_weather_map_api = '8a707d148cd925c48443efd55cbb75b9'

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

    now = datetime.today().strftime('Сейчас в Москве: ' + '%d.%m.%Y %H:%M:%S')
    message = '{}\n{}\n{}\n' \
          'Температура: {}°C\n' \
          'Ощущается как: {}°C\n' \
          'Ветер: {} м/с\n' \
          'Порывы до {} м/с\n' \
          'Влажность: {}%\n' \
          'Давление: {} мм.рт.столба\n' \
          'Облачность: {}%\n' \
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
                .strftime('%H:%M') if get_data(r, 'sys', 'sunset') != '—' else 'Ошибка!')
    return message

def get_data(data, *keys):
    for key in keys:
        if key in data:
            data = data[key]
        else:
            return '—'
    return data