from datetime import datetime
import requests
import json

with open('config.json', 'r') as data:
    config = data.read()
    data.close()
    config = json.loads(config)
    debug = config['debug']
__print = print
print = lambda a: __print(a) if debug else 0

URL = 'https://api.openweathermap.org/data/2.5/onecall?'

QUERY_TEMPLATE = {
    'appid': '12934e34e68da8ef0415c09031f4bfd2',
    'lat': '37.9149',
    'lon': '127.0667',
    'units': 'metric',
    'exclude': 'minutely,hourly',
    'lang': 'eng'
}
DT_TEMPLATE = '%y%m%d, %H:%M:%S'

class weather_api():
    def __init__(self):
        self.min = [None]*8
        self.max = [None] * 8
        self.query = dict(QUERY_TEMPLATE)
        self.dt = str(DT_TEMPLATE)
        self.res = requests.get(URL, params=self.query).json()

    def api_call(self):
        
        print('Wapi Called')
        self.res['current']['dt'] = (datetime.utcfromtimestamp(self.res['current']['dt'])).strftime(self.dt)
        self.res['current']['sunrise'] = (datetime.utcfromtimestamp(self.res['current']['sunrise'])).strftime(self.dt)
        self.res['current']['sunset'] = (datetime.utcfromtimestamp(self.res['current']['sunset'])).strftime(self.dt)
        print(self.res)
        for i in range(8):
            self.res['daily'][i]['dt'] = (datetime.utcfromtimestamp(self.res['daily'][i]['dt'])).strftime(self.dt)
            self.min[i] = self.res['daily'][i]['temp']['min']
            self.max[i] = self.res['daily'][i]['temp']['max']

