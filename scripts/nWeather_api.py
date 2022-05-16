from datetime import datetime, timedelta
import copy
import requests
import re
import time
import pathlib
import pytz

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
    def __init__(self, ):
        self.api_call()

    def api_call(self, ):
        query = copy.deepcopy(query_template)
        dttemplate = copy.deepcopy(dt_template)
        res = requests.get(url, params=query).json()
        res['current']['dt'] = (datetime.utcfromtimestamp(res['current']['dt'])).strftime(dttemplate)
        res['current']['sunrise'] = (datetime.utcfromtimestamp(res['current']['sunrise'])).strftime(dttemplate)
        res['current']['sunset'] = (datetime.utcfromtimestamp(res['current']['sunset'])).strftime(dttemplate)
        for i in range(8):
            res['daily'][i]['dt'] = (datetime.utcfromtimestamp(res['daily'][i]['dt'])).strftime(dttemplate)
        print(res)

weather_api()
