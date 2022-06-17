import requests
import json
import datetime
import yaml
from datetime import date
lat1 = 8.4095
lon = 115.1889


with open('../credentials/configTest.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

key = config['apiWeather']
key_water = config['apiWaves']


response_water = requests.get(f"https://api.stormglass.io/v2/weather/point?lat={lat1}&lng={lon}&params=windSpeed"
                              f"Authorization: {key_water}")
response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat1}&lon={lon}&appid={key}')
print(response_water.text)
info = response.json()
info_water = response_water.json()
#water_temp = info_water['waterTemperature']
#print(water_temp)
print(info_water.keys())



wind_speed = info['current']['wind_speed']
time_sunrise = info['current']['sunrise']
time_sunset = info['current']['sunset']
sunrise = datetime.datetime.fromtimestamp(time_sunrise)
sunset = datetime.datetime.fromtimestamp(time_sunset)
current_time = datetime.datetime.now()
if wind_speed > 4.00:
    print(f'Time sunrise is {sunrise.time()}, time sunset is {sunset.time()}, wind is so strong for surfing {wind_speed}')
else:
    print(f'Time sunrise is {sunrise.time()}, time sunset is {sunset.time()}, wind speed is good for surfing {wind_speed}')
current_time1 = str(current_time.time())
print(f'Current time is {current_time1[:8]}')
if sunrise < current_time < sunset :
    print('Go to surf')
else:
    print('Too dark')