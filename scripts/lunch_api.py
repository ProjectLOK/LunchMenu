from datetime import datetime, timedelta
import copy
import requests
import re

url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
serviceKey = '128332e82a2f42bcbc58d826a24084ce'
ATPT_OFCDC_SC_CODE = 'J10'
SD_SCHUL_CODE = '7530544'

query_template = {
        'Key': serviceKey,
        'Type': 'json',
        'pIndex': 1,
        'pSize': 2,
        'ATPT_OFCDC_SC_CODE': ATPT_OFCDC_SC_CODE,
        'SD_SCHUL_CODE': SD_SCHUL_CODE,
        'MMEAL_SC_CODE': '',
        'MLSV_FROM_YMD': '',
        'MLSV_TO_YMD': '',
    }


class lunch_api():
    def __init__(self, data=None, date=None, dish=None, cal=None):
        self.api_call()

    def api_call(self):
        self.req_date = datetime.today()
        query = copy.deepcopy(query_template)
        query['MLSV_FROM_YMD'] = self.req_date.strftime('%Y%m%d')
        query['MLSV_TO_YMD'] = (self.req_date + timedelta(days=3)).strftime('%Y%m%d')
        res = requests.get(url, params=query).json()

        try:
            self.data = res['mealServiceDietInfo']

        except KeyError:
            CODE = res['RESULT']['CODE']
            MESSAGE = res['RESULT']['MESSAGE']
            print('<API CALL FAILURE> {}: {}'.format(CODE, MESSAGE))
            return 1

        else:
            CODE = self.data[0]['head'][1]['RESULT']['CODE']
            MESSAGE = self.data[0]['head'][1]['RESULT']['MESSAGE']
            print('<API CALL SUCCESS> {}: {}'.format(CODE, MESSAGE))
            print(res)
            self.date = ['']*query['pSize']
            self.dish = ['']*query['pSize']
            self.cal = ['']*query['pSize']
            for i in range(query['pSize']):
                self.dish[i] = self.data[1]['row'][i]['DDISH_NM']
                self.dish[i] = re.sub(r'[0-9*.<br>()]+', '', self.dish[i])
                self.dish[i] = re.sub(r'[/]+', '\n', self.dish[i])
                self.cal[i] = self.data[1]['row'][i]['CAL_INFO']
                self.date[i] = self.data[1]['row'][i]['MLSV_YMD']
                self.date[i] = self.date[i][4:6] + '.' + self.date[i][6:]