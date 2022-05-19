import asyncio
from tkinter import *
from tkinter import ttk as tk
from scripts.lunch_api import lunch_api
root = Tk()


main = ('Arial', 70)
small = ('Arial', 45)
lunch = lunch_api()

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class LunchPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.date_today = tk.Label(self, text=lunch.date[0], font=small)
        self.date_next = tk.Label(self, text=lunch.date[1], font=small)
        self.dish_today = tk.Label(self, text=lunch.dish[0], padding=10, font=main, anchor=N)
        self.dish_next = tk.Label(self, text=lunch.dish[1], padding=10, font=main, anchor=N)
        self.date_today.grid(column=0, row=0)
        self.date_next.grid(column=2, row=0)
        self.dish_today.grid(column=0, row=1)
        self.dish_next.grid(column=2, row=1)
        tk.Label(self, text='>', padding=10, font=main, anchor=N).grid(column=1, row=1)
        frm.pack(expand=YES, fill=BOTH)


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

if __name__ == '__main__':
    asyncio.run(main())