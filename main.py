from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import schedule as schedule
import time
from scripts.lunch_api import lunch_api

root = Tk()
root.title('Diet')
main = ('Arial', 70)
small = ('Arial', 45)

lunch = lunch_api()
# import sys
# from PyQt5.QtWidgets import QAplication, QWidget

def display():
    frm = ttk.Frame(root, padding=20)
    frm.pack(expand=YES, fill=BOTH)
    frm.grid(column=0, row=0)
    ttk.Label(frm, text=lunch.date.strftime('%m.%d'), font=small).grid(column=0, row=0)
    ttk.Label(frm, text=(lunch.date + timedelta(days=1)).strftime('%m.%d'), font=small).grid(column=2, row=0)
    ttk.Label(frm, text=lunch.dish[0], padding=10, font=main, anchor=N).grid(column=0, row=1)
    ttk.Label(frm, text='>', padding=10, font=main, anchor=N).grid(column=1, row=1)
    ttk.Label(frm, text=lunch.dish[1], padding=10, font=main, anchor=N).grid(column=2, row=1)
    root.mainloop()

display()

'''
schedule.every(10).seconds.do(lunch.api_call())
schedule.every(11).seconds.do(dish, 1)
schedule.every(12).seconds.do(dish, 2)
schedule.every(13).seconds.do(display)
while True:
    schedule.run_pending()
    time.sleep(1)
'''
# schedule.every().day.at("7:00").do(update)