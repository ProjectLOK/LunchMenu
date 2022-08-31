from datetime import datetime, timedelta
import copy
import requests
import re
import time

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
serviceKey = 'AeAcK+vRcfPws0o8ZNy24LcNVm/roD5Ty0exy/86eS0YUcRLanD585e3I/X1IbMJVENlMwoSaUP5Bx6oZCUuLQ=='
date = datetime.today()
curr_time = datetime.now().strftime('%H')
time_template = ['0200', '0500', '0800', '1100', '1400', '1700', '2000', '2300']
req_time = time_template[int(curr_time)//3]


query_template = {
    'serviceKey': serviceKey,
    'numOfRows': '180',
    'pageNO': '1',
    'dataType': 'JSON',
    'base_date': '20220427',
    'base_time': time_template[0],
    'nx': '61',
    'ny': '134',
}

weather_template = {
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
    tmxtmn = None
    def api_call(self):
        query = copy.deepcopy(query_template)
        self.tmxtmn = copy.deepcopy(weather_template)
        self.req_today = date.strftime('%Y%m%d')
        self.req_next = (date + timedelta(days=1)).strftime('%Y%m%d')
        data = copy.deepcopy(weather_template)
        try:
            res = requests.get(url, params=query).json()
        except ConnectionError:
            time.sleep(30)
            self.api_call()
        try:
            self.raw_data = res['response']['body']['items']['item']
        except KeyError:
            return 1
        except RequestsJSONDecodeError(err):
            print(err)
        else:
            for i in range(180):
                self.tmxtmn[self.raw_data[i]['category']] = self.raw_data[i]['fcstValue']