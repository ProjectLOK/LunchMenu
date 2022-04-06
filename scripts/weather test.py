import requests

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
params ={'serviceKey' : 'AeAcK+vRcfPws0o8ZNy24LcNVm/roD5Ty0exy/86eS0YUcRLanD585e3I/X1IbMJVENlMwoSaUP5Bx6oZCUuLQ==', 'dataType': 'JSON', 'pageNo' : '1', 'numOfRows' : '1000', 'base_date' : '20220406', 'base_time' : '0500', 'nx' : '61', 'ny' : '134' }

response = requests.get(url, params=params).json()
print(response)