from datetime import datetime, timedelta
import copy
import requests
import re

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
serviceKey = 'AeAcK+vRcfPws0o8ZNy24LcNVm/roD5Ty0exy/86eS0YUcRLanD585e3I/X1IbMJVENlMwoSaUP5Bx6oZCUuLQ=='
date = datetime.today().strftime('%Y%m%d')
time = datetime.now().strftime('%H00')
query = {
    'serviceKey': serviceKey,
    'numOfRows': '14',
    'pageNO': '1',
    'dataType': 'JSON',
    'base_date': date,
    'base_time': '0800',
    'nx': '61',
    'ny': '134',
}
print(query)
res = requests.get(url, params=query).json()

