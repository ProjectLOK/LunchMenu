import tkinter as tk
import asyncio
import widgets
import json

async def main():
    root = tk.Tk()
    root.title('Lunch Menu') 
    root.geometry('1872x1404')
    root.resizable(False, False)
    today_lunch = widgets.TodayLunch(root)
    clock = widgets.Clock(root)
    nextday_lunch = widgets.NextdayLunch(root)
    today_lunch.grid(row=0, rowspan=2, column=0)
    clock.grid(row=0, column=1, columnspan=2)
    nextday_lunch.grid(row=1, column=1)

    while True:
        root.update()
        await asyncio.sleep(0.01)

if __name__ == "__main__":
    asyncio.run(main())
    exit(0)
