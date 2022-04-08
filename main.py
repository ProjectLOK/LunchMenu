import time
from tkinter import *
from tkinter import ttk
from scripts.lunch_api import lunch_api
import asyncio
from scripts.weather_api import weather_api

root = Tk()
root.title('Diet')
root.geometry('1872x1404')
main = ('Arial', 70)
small = ('Arial', 45)
lunch = lunch_api()
weather = weather_api()
frm = ttk.Frame(root, padding=20)
date_today = ttk.Label(frm, text=lunch.date[0], font=small)
date_next = ttk.Label(frm, text=lunch.date[1], font=small)
dish_today = ttk.Label(frm, text=lunch.dish[0], padding=10, font=main, anchor=N)
dish_next = ttk.Label(frm, text=lunch.dish[1], padding=10, font=main, anchor=N)
tmx_today = ttk.Label(frm, text=weather.tmxtmn['TMX'])
tmn_today = ttk.Label(frm, text=weather.tmxtmn['TMN'])
tmx_next = ttk.Label(frm, text=weather.tmxtmn['TMX'])
tmn_next = ttk.Label(frm, text=weather.tmxtmn['TMN'])
date_today.grid(column=0, row=0)
date_next.grid(column=2, row=0)
dish_today.grid(column=0, row=1)
dish_next.grid(column=2, row=1)
ttk.Label(frm, text='>', padding=10, font=main, anchor=N).grid(column=1, row=1)
frm.pack(expand=YES, fill=BOTH)


async def main():
    gui_task = asyncio.create_task(GUI())
    while True:
        await update()

async def GUI():
    while True:
        root.update()
        await asyncio.sleep(0.001)


async def update():
    await asyncio.sleep(15)
    lunch.api_call()
    dish_today.configure(text=lunch.dish[0])
    dish_next.configure(text=lunch.dish[1])
    root.update()
    print("update success")

if __name__ == '__main__':
    asyncio.run(main())

print(weather.tmxtmn['TMX'])
