import requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : 'AeAcK+vRcfPws0o8ZNy24LcNVm/roD5Ty0exy/86eS0YUcRLanD585e3I/X1IbMJVENlMwoSaUP5Bx6oZCUuLQ==', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : '20210628', 'base_time' : '0600', 'nx' : '55', 'ny' : '127' }

response = requests.get(url, params=params)
print(response.content)