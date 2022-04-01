from tkinter import *
from tkinter import ttk
from scripts.lunch_api import lunch_api
import asyncio

root = Tk()
root.title('Diet')
main = ('Arial', 70)
small = ('Arial', 45)
lunch = lunch_api()

frm = ttk.Frame(root, padding=20)
date_today = ttk.Label(frm, text=lunch.date[0], font=small)
date_next = ttk.Label(frm, text=lunch.date[1], font=small)
dish_today = ttk.Label(frm, text=lunch.dish[0], padding=10, font=main, anchor=N)
dish_next = ttk.Label(frm, text=lunch.dish[1], padding=10, font=main, anchor=N)


async def display():
    date_today.grid(column=0, row=0)
    date_next.grid(column=2, row=0)
    dish_today.grid(column=0, row=1)
    dish_next.grid(column=2, row=1)
    ttk.Label(frm, text='>', padding=10, font=main, anchor=N).grid(column=1, row=1)
    frm.pack(expand=YES, fill=BOTH)
    root.mainloop()


async def update():
    lunch.api_call()
    date_today.text = 'asdfas'
    await asyncio.sleep(1000)

asyncio.run(display())
print(1)
while True:
    update()


'''
# schedule.every().day.at("7:00").do(update)
'''