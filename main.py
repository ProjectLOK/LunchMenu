import tkinter as tk
import time
import asyncio
import aioschedule as sch
import lunchpage
import weatherpage
from scripts.lunch_api import lunch_api
from scripts.nWeather_api import weather_api
lunch = lunch_api()
wt = weather_api()
lp = None
wp = None

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        global lp
        global wp
        tk.Frame.__init__(self, *args, **kwargs)
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        lp = lunchpage.LunchPage(self)
        wp = weatherpage.WeatherPage(self)
        b1 = tk.Button(buttonframe, text="급식", command=lp.show)
        b2 = tk.Button(buttonframe, text="날씨", command=wp.show)

        lp.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        wp.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1.pack(side="left")
        b2.pack(side="left")
        lp.show()


async def update():
    lunch.api_call()
    wt.api_call()
    lp.dish_today.configure(text=lunch.dish[0])
    lp.dish_next.configure(text=lunch.dish[1])
    lp.date_today.configure(text=lunch.date[0])
    lp.date_next.configure(text=lunch.date[1])
    wp.min_today.configure(text=wt.min[0])
    wp.max_today.configure(text=wt.max[1])
    print("update success")

async def main():
    sch.every().day.at("03:00").do(update)
    await GUI()


async def GUI():
    while True:
        await sch.run_pending()
        root.update()

if __name__ == "__main__":
    root = tk.Tk()
    view = MainView(root)
    root.geometry('1872x1404')
    root.title('Info')
    view.pack(side="top", fill="both", expand=True)
    asyncio.run(main())

