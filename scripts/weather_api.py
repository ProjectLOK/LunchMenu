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
    'base_date': '20220429',
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

    def __init__(self, humidity = None):
        self.api_call()
        self.req_today, self.req_next, self.raw_data = None, None, None,

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
            return 1
        try:
            self.raw_data = res['response']['body']['items']['item']
        except KeyError:
            return 1
        except RequestsJSONDecodeError(err):
            print(err)

        # 최고기온, 최저기온만을 위해 쨔여진 코드
        for i in range(180):
            self.tmxtmn[self.raw_data[i]['category']] = self.raw_data[i]['fcstValue']


'''
flag = 1
while flag:
    flag = api_call()
api = weather_api()
'''


#Code = res['response']['header']['resultCode']
#Message = res['response']['header']['resultMsg']

#print('<Weather API CALL Succes> {}: {}'.format(Code, Message))
