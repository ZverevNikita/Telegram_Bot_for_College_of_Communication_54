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
                r['name'],
                r['weather'][0]['description'].capitalize(),
                r['main']['temp'],
                r['main']['feels_like'],
                r['wind']['speed'],
                r['wind']['gust'],
                r['main']['humidity'],
                r['main']['pressure'],
                r['clouds']['all'],
                datetime.fromtimestamp(r['sys']['sunset']).strftime('%H:%M'))
    return msg
