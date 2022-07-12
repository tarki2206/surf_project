import os

import requests
import json
import datetime
import yaml
from datetime import date

REQUIRED_LATITUDE = 8.4095
REQUIRED_LONGITUDE = 115.1889

with open('../credentials/configTest.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

OPEN_WEATHER_KEY = config['apiWeather']
STORMGLASS_KEY = config['apiWaves']


def search_weather_by_time(response_water, requested_time: str):
    count = 0
    for time_period in response_water.json()['hours']:
        # if time_period['time'] == requested_time:
        #     print('нашли')
        print(time_period)
        count += 1
    print(count)


def create_local_json_file(path_to_folder: str, file_name: str, url: str, params: dict, headers: dict) -> None:
    response_storm_glass = requests.get(
        url=url,
        params=params,
        headers=headers
    )

    path = path_to_folder + '/' + file_name

    with open(path, 'w+') as json_file:
        json.dump(response_storm_glass.json(), json_file, indent=4)


def get_data_from_stormglass():
    url_storm_glass = 'https://api.stormglass.io/v2/weather/point'
    params_storm_glass = {
        'lat': REQUIRED_LATITUDE,
        'lng': REQUIRED_LONGITUDE,
        'params': ['waveHeight', 'wind_speed', 'wavePeriod']
    }
    headers_storm_glass = {'Authorization': STORMGLASS_KEY}

    if os.path.isdir('../static'):
        if os.path.isfile('../static/StormGlassData.json'):
            print('reading from local file')
        else:
            create_local_json_file(
                path_to_folder='../static',
                file_name='StormGlassData.json',
                url=url_storm_glass,
                params=params_storm_glass,
                headers=headers_storm_glass
            )
    else:
        os.mkdir('../static')
        create_local_json_file(
            path_to_folder='../static',
            file_name='StormGlassData.json',
            url=url_storm_glass,
            params=params_storm_glass,
            headers=headers_storm_glass
        )
    return 0


def get_data_from_openweathermap():
    url_openweather = 'https://api.openweathermap.org/data/3.0/onecall'
    params_openweather = {'lat': REQUIRED_LATITUDE, 'lon': REQUIRED_LONGITUDE, 'appid': OPEN_WEATHER_KEY}

    response = requests.get(
        url=url_openweather,
        params=params_openweather
    )
    return response


if __name__ == '__main__':

    print(get_data_from_openweathermap().text)
    print(get_data_from_stormglass())

    # requested_time = '2022-06-21T00:00:00+00:00'

    # response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat1}&lon={lon}&appid={key}')
    # print(response_water.text)
    # info = response.json()
    # info_water = response_water.json()
    # #water_temp = info_water['waterTemperature']
    # #print(water_temp)
    # print(info_water.keys())
    #
    #
    #
    # wind_speed = info['current']['wind_speed']
    # time_sunrise = info['current']['sunrise']
    # time_sunset = info['current']['sunset']
    # sunrise = datetime.datetime.fromtimestamp(time_sunrise)
    # sunset = datetime.datetime.fromtimestamp(time_sunset)
    # current_time = datetime.datetime.now()
    # if wind_speed > 4.00:
    #     print(f'Time sunrise is {sunrise.time()}, time sunset is {sunset.time()}, wind is so strong for surfing {wind_speed}')
    # else:
    #     print(f'Time sunrise is {sunrise.time()}, time sunset is {sunset.time()}, wind speed is good for surfing {wind_speed}')
    # current_time1 = str(current_time.time())
    # print(f'Current time is {current_time1[:8]}')
    # if sunrise < current_time < sunset :
    #     print('Go to surf')
    # else:
    #     print('Too dark')