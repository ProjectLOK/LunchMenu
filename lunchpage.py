import asyncio
from tkinter import *
<<<<<<< Updated upstream
from tkinter import ttk
=======
from tkinter import ttk as tk
import tkinter.font as tkFont
import time
>>>>>>> Stashed changes
from scripts.lunch_api import lunch_api

root = Tk()
root.title('Diet')
root.geometry('1872x1404')
main = ('Arial', 70)
small = ('Arial', 45)
lunch = lunch_api()
<<<<<<< Updated upstream
frm = ttk.Frame(root, padding=20)
date_today = ttk.Label(frm, text=lunch.date[0], font=small)
date_next = ttk.Label(frm, text=lunch.date[1], font=small)
dish_today = ttk.Label(frm, text=lunch.dish[0], padding=10, font=main, anchor=N)
dish_next = ttk.Label(frm, text=lunch.dish[1], padding=10, font=main, anchor=N)
date_today.grid(column=0, row=0)
date_next.grid(column=2, row=0)
dish_today.grid(column=0, row=1)
dish_next.grid(column=2, row=1)
ttk.Label(frm, text='>', padding=10, font=main, anchor=N).grid(column=1, row=1)
frm.pack(expand=YES, fill=BOTH)
=======
lunch.api_call()


class LunchPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        empty_label = tk.Label(self)
        date = time.strftime("%m월 %d일 %a요일")
        time_data = time.strftime("%I:%M")
        time_label = tk.Label(self, text=time_data, font=small)
        lunchframe = tk.Frame()
        lunchframe.pack()

        date_today = tk.Label(lunchframe, text=lunch.date[0], font=small, borderwidth=2)
        date_next = tk.Label(lunchframe, text=lunch.date[1], font=small, borderwidth=2)
        dish_today = tk.Label(lunchframe, text=lunch.dish[0], padding=10, font=main, borderwidth=2, justify="center")
        dish_next = tk.Label(lunchframe, text=lunch.dish[1], padding=10, font=main, borderwidth=2, justify="center")
        arrow = tk.Label(lunchframe, text='\n→', padding=25, font=main, borderwidth=2)
        cal_today = tk.Label(lunchframe, text=lunch.cal[0], font=small, justify="center")
        cal_next = tk.Label(lunchframe, text=lunch.cal[1], font=small, justify="center")

        empty_label.grid(row=0, column=0, rowspan=2, padx=20) #for left padding
        date_today.grid(row=0, column=1)
        arrow.grid(rowspan=2, row=0, column=2)
        date_next.grid(row=0, column=3)
        dish_today.grid(row=1, column=1)
        dish_next.grid(row=1, column=3)
        cal_today.grid(row=2, column=1)
        cal_next.grid(row=2, column=3)
>>>>>>> Stashed changes

        time_label.grid(row=0, column=0)
        lunchframe.grid(row=1, column=0)


async def update():
    lunch.api_call()
    dish_today.configure(text=lunch.dish[0])
    dish_next.configure(text=lunch.dish[1])
    date_today.configure(text=lunch.date[0])
    date_next.configure(text=lunch.date[1])
    print("update success")
