from datetime import datetime, timedelta
import copy
import requests
import re

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
serviceKey = 'AeAcK+vRcfPws0o8ZNy24LcNVm/roD5Ty0exy/86eS0YUcRLanD585e3I/X1IbMJVENlMwoSaUP5Bx6oZCUuLQ=='
date = datetime.today().strftime('%Y%m%d')
time = datetime.now().strftime('%H00')
query_template= {
    'serviceKey': serviceKey,
    'numOfRows': '14',
    'pageNO': '1',
    'dataType': 'JSON',
    'base_date': date,
    'base_time': '1100',
    'nx': '61',
    'ny': '134',
}

class weather_api():
    def __init__(self, data=None, humidity = None):
        self.api_call()

    def api_call(self):
        query = copy.deepcopy(query_template)
        res = requests.get(url, params=query).json()

        try:
            self.data = res['response']['body']['items']['item']
        except KeyError:
            print('e')
            return 1

        else:
            for i in range(14):
                if self.data['category'] == REH:
                    self.humidity = self.data['fcstValue']
                    print(self.humidity)
                    print('0')



#Code = res['response']['header']['resultCode']
#Message = res['response']['header']['resultMsg']

#print('<Weather API CALL Succes> {}: {}'.format(Code, Message))
