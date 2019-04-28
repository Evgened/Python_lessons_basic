
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json

# это невероятно, но у меня что-то получилось!
# ответ от openWeatherMap:
# {'coord': {'lon': 7.18, 'lat': 51.52}, 'weather': [{'id': 521, 'main': 'Rain', 'description': 'shower rain', 'icon': '09d'}], 'base': 'stations', 'main': {'temp': 12.52, 'pressure': 1019, 'humidity': 58, 'temp_min': 10.56, 'temp_max': 15}, 'visibility': 10000, 'wind': {'speed': 1}, 'clouds': {'all': 0}, 'dt': 1556469983, 'sys': {'type': 1, 'id': 1306, 'message': 0.007, 'country': 'DE', 'sunrise': 1556424566, 'sunset': 1556477277}, 'id': 2932029, 'name': 'Eickel', 'cod': 200}
# время поджимает, сдаю так, но буду делать дальше

import os
import requests

city_dir = 'city'

city_list = dict.fromkeys(['id', 'name', 'country', 'coord'])

# {'id': 2784102, 'name': 'Wanne', 'country': 'BE', 'coord': {'lon': 5.92083, 'lat': 50.355}}

# Читаем JSON из файла и преобразуем к типу Python
with open(os.path.join(city_dir, 'city.list.json'), 'r', encoding='UTF-8') as f:
    city_list = json.load(f)

print (city_list[0])

city_one = dict (city_list[0])

print (city_one["id"])

url_c = str('http://api.openweathermap.org/data/2.5/weather?id=') + str(city_one["id"]) + str('&units=metric&appid=6b3dea879d565ee08bc8499f39ac2570')

print(url_c)

response_c = requests.get(url_c)
temp_c = json.loads(response_c.text)

print (temp_c)

