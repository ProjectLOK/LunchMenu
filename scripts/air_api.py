from datetime import datetime, timedelta
import requests
import time
import json

with open('config.json', 'r') as data:
    config = data.read()
    data.close()
    config = json.loads(config)
    debug = config['debug']
__print = print
print = lambda a: __print(a) if debug else 0
URL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
SERVICE_KEY = 'AeAcK+vRcfPws0o8ZNy24LcNVm/roD5Ty0exy/86eS0YUcRLanD585e3I/X1IbMJVENlMwoSaUP5Bx6oZCUuLQ=='
date = datetime.today()
curr_time = datetime.now().strftime('%H')
TIME_TEMPLATE = ['0200', '0500', '0800', '1100', '1400', '1700', '2000', '2300']
req_time = TIME_TEMPLATE[int(curr_time)//3]


QUERY_TEMPLATE = {
    'serviceKey': SERVICE_KEY,
    'numOfRows': '180',
    'pageNO': '1',
    'dataType': 'JSON',
    'base_date': '20220427',
    'base_time': TIME_TEMPLATE[0],
    'nx': '61',
    'ny': '134',
}

WEATHER_TEMPLATE = {
    'POP': None,
    'PCP': None,
    'REH': None,
    'SNO': None,
    'SKY': None,
    'TMP': None,
    'TMN': None,
    'TMX': None,
    'UUU': None,
    'VVV': None,
    'WAV': None,
    'VEC': None,
    'WSD': None
}


class weather_api():
    def __init__(self):
        self.query = dict(QUERY_TEMPLATE)
        self.tmxtmn = dict(WEATHER_TEMPLATE)
        data = dict(WEATHER_TEMPLATE)

    def api_call(self):
        self.req_today = date.strftime('%Y%m%d')
        self.req_next = (date + timedelta(days=1)).strftime('%Y%m%d')
        try:
            res = requests.get(URL, params=self.query).json()
        except ConnectionError:
            time.sleep(30)
            self.api_call()
        try:
            self.raw_data = res['response']['body']['items']['item']
        except KeyError:
            return 1
        else:
            for i in range(180):
                self.tmxtmn[self.raw_data[i]['category']] = self.raw_data[i]['fcstValue']