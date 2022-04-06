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
    'numOfRows': '1',
    'pageNO': '14',
    'dataType': 'JSON',
    'base_date': date,
    'base_time': '1100',
    'nx': '61',
    'ny': '134',
}

res = requests.get(url, params=query_template).json()
print(res['response'])