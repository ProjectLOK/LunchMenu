import re
from tkinter import *
from tkinter import ttk
import requests
import sys
from PyQt5.QtWidgets import QAplication, QWidget
from datetime import datetime
date = datetime.today().strftime("%Y%m%d")
serviceKey = '128332e82a2f42bcbc58d826a24084ce'
url = 'https://open.neis.go.kr/hub/mealServiceDietInfo?'
params = {'Key': serviceKey,
          'Type': 'json',
          'pIndex': 1,
          'pSize': 5,
          'ATPT_OFCDC_SC_CODE': 'J10',
          'SD_SCHUL_CODE': 7530544,
          'MLSV_YMD': date
          }
req = requests.get(url, params=params).json()['mealServiceDietInfo']
diet = req[1]['row'][0]['DDISH_NM']
diet = re.sub(r'[0-9*.<br>]+', '', diet)

root = Tk()
root.title('Diet')

frm = ttk.Frame(root, padding=10)
frm.grid(column=0, row=0)
ttk.Label(frm, text=diet).grid(column=0, row=0)
ttk.Button(frm, text='quit', command=root.destroy).grid(column=1, row=1)
root.mainloop()

print(diet)
print(req[1]['row'][0]['CAL_INFO'])