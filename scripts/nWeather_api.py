from datetime import datetime, timedelta
import copy
import requests
import time
import json

with open('config.json', 'r') as config:
    config = config.read()
    config = json.loads(config)
    debug = config['debug']
temp = print
print = lambda a: temp(a) if debug else 0
del temp

url = 'https://api.openweathermap.org/data/2.5/onecall?'

query_template = {
    'appid': '12934e34e68da8ef0415c09031f4bfd2',
    'lat': '37.9149',
    'lon': '127.0667',
    'units': 'metric',
    'exclude': 'minutely,hourly',
    'lang': 'eng'
}
dt_template = ('%y%m%d, %H:%M:%S')

class weather_api():
    def __init__(self):
        self.min = [None]*8
        self.max = [None] * 8
        #self.api_call()

    def api_call(self):
        query = copy.deepcopy(query_template)
        dttemplate = copy.deepcopy(dt_template)
        res = requests.get(url, params=query).json()
        print('Wapi Called')
        res['current']['dt'] = (datetime.utcfromtimestamp(res['current']['dt'])).strftime(dttemplate)
        res['current']['sunrise'] = (datetime.utcfromtimestamp(res['current']['sunrise'])).strftime(dttemplate)
        res['current']['sunset'] = (datetime.utcfromtimestamp(res['current']['sunset'])).strftime(dttemplate)
        print(res)
        for i in range(8):
            res['daily'][i]['dt'] = (datetime.utcfromtimestamp(res['daily'][i]['dt'])).strftime(dttemplate)
            self.min[i] = res['daily'][i]['temp']['min']
            self.max[i] = res['daily'][i]['temp']['max']

