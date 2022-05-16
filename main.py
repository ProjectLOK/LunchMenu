import time
import asyncio
from scripts.nWeather_api import weather_api
import aioschedule as sch
import lunchpage
import tkinter as tk
import page_demo

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        lp = lunchpage.LunchPage(self)
        lp.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        b1 = tk.Button(buttonframe, text="급식", command=lp.show)
        b1.pack(side="left")
        p2 = page_demo.Page2(self)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        b2.pack(side="left")
        lp.show()
async def update():
    lunch.api_call()
    dish_today.configure(text=lunch.dish[0])
    dish_next.configure(text=lunch.dish[1])
    date_today.configure(text=lunch.date[0])
    date_next.configure(text=lunch.date[1])
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
    main = MainView(root)
    root.geometry('1872x1404')
    main.pack(side="top", fill="both", expand=True)
    asyncio.run(main())
    root.mainloop()
