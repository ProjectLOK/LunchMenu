from datetime import datetime, timedelta
import requests
import re
import json

with open('config.json', 'r') as data:
    config = data.read()
    data.close()
    config = json.loads(config)
    debug = config['debug']
__print = print
print = lambda a: __print(a) if debug else 0

URL = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
SERVICE_KEY = '128332e82a2f42bcbc58d826a24084ce'
ATPT_OFCDC_SC_CODE = 'J10'
SD_SCHUL_CODE = '7530544'

QUERY_TEMPLATE = {
        'Key': SERVICE_KEY,
        'Type': 'json',
        'pIndex': 1,
        'pSize': 6,
        'ATPT_OFCDC_SC_CODE': ATPT_OFCDC_SC_CODE,
        'SD_SCHUL_CODE': SD_SCHUL_CODE,
        'MMEAL_SC_CODE': '',
        'MLSV_FROM_YMD': '',
        'MLSV_TO_YMD': '',
    }


class lunch_api():
    def api_call(self):
        self.req_date = datetime.today()
        query = dict(QUERY_TEMPLATE)
        query['MLSV_FROM_YMD'] = self.req_date.strftime('%Y%m%d')
        query['MLSV_TO_YMD'] = (self.req_date + timedelta(days=7)).strftime('%Y%m%d')
        res = requests.get(URL, params=query).json()
        print(res)

        try:
            self.data = res['mealServiceDietInfo']

        except KeyError:
            code = res['RESULT']['CODE']
            message = res['RESULT']['MESSAGE']
            print('<API CALL FAILURE> {}: {}'.format(code, message))
            return 1

        else:
            code = self.data[0]['head'][1]['RESULT']['CODE']
            message = self.data[0]['head'][1]['RESULT']['MESSAGE']
            print('<API CALL SUCCESS> {}: {}'.format(code, message))
            self.dish = ['']*query['pSize']
            self.cal = ['']*query['pSize']
            for i in range(query['pSize']):
                try:
                    self.dish[i] = self.data[1]['row'][i]['DDISH_NM']
                    self.cal[i] = self.data[1]['row'][i]['CAL_INFO']
                except IndexError:
                    self.dish[i] = "정보가 없습니다."
                    self.cal[i] = "0"
                self.dish[i] = re.sub(r'[0-9*.<br>() ]+', '', self.dish[i])
                self.dish[i] = re.sub(r'[/]+', '\n', self.dish[i])
                try:
                    self.dish[i] = self.dish[i][:self.dish[i].index("+")] + "\n" + self.dish[i][self.dish[i].index("+"):]
                except ValueError:
                    pass

if __name__ == "__main__":
    api = lunch_api()
    api.api_call()
