from datetime import datetime, timedelta
import copy
import requests
import re

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0'
serviceKey = 'AeAcK%2BvRcfPws0o8ZNy24LcNVm%2FroD5Ty0exy%2F86eS0YUcRLanD585e3I%2FX1IbMJVENlMwoSaUP5Bx6oZCUuLQ%3D%3D'
date = datetime.today().strftime('%Y%m%d')
query_template = {
    'serviceKey': serviceKey,
    'dataType': 'json',
    'base_date': 'date',
    'base_time': '0800',
    'nx': '61',
    'ny': '134',
}
