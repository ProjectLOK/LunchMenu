import asyncio
from tkinter import *
from tkinter import ttk
from scripts.lunch_api import lunch_api

root = Tk()
root.title('Diet')
root.geometry('1872x1404')
main = ('Arial', 70)
small = ('Arial', 45)
lunch = lunch_api()
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


async def update():
    lunch.api_call()
    dish_today.configure(text=lunch.dish[0])
    dish_next.configure(text=lunch.dish[1])
    date_today.configure(text=lunch.date[0])
    date_next.configure(text=lunch.date[1])
    print("update success")
