import re
from tkinter import *
from tkinter import ttk
import requests
#import sys
#from PyQt5.QtWidgets import QAplication, QWidget
from datetime import datetime, timedelta

date = datetime.today()
serviceKey = '128332e82a2f42bcbc58d826a24084ce'
url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
params = {'Key': serviceKey,
          'Type': 'json',
          'pIndex': 1,
          'pSize': 5,
          'ATPT_OFCDC_SC_CODE': 'J10',
          'SD_SCHUL_CODE': 7530544,
          'MLSV_FROM_YMD': date.strftime('%Y%m%d'),
          'MLSV_TO_YMD': (date + timedelta(days=1)).strftime('%Y%m%d')
          }
print(params)
req = requests.get(url, params=params).json()['mealServiceDietInfo']


def dish(i):
    tmp = req[1]['row'][i]['DDISH_NM']
    tmp = re.sub(r'[0-9*.<br>]+', '', tmp)
    tmp = re.sub(r'[/]+', '\n', tmp)
    cal = req[1]['row'][i]['CAL_INFO']
    return {'diet': tmp, 'cal': cal}


root = Tk()
root.title('Diet')
main = ('Arial', 90)
small = ('Arial', 20)

frm = ttk.Frame(root, padding=20)
frm.grid(column=0, row=0)
ttk.Label(frm, text = '오늘', font=small).grid(column=0, row=0)
ttk.Label(frm, text = '내일', font=small).grid(column=1, row=0)
ttk.Label(frm, text=dish(0)['diet'], padding=10, font=main).grid(column=0, row=1)
ttk.Label(frm, text=dish(1)['diet'], padding=10, font=main, anchor=N).grid(column=1, row=1)


root.mainloop()
