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
        empty_label = tk.Label(self)
        date_today = tk.Label(self, text=lunch.date[0], font=small, borderwidth=2)
        date_next = tk.Label(self, text=lunch.date[1], font=small, borderwidth=2)
        dish_today = tk.Label(self, text=lunch.dish[0], padding=10, font=main, borderwidth=2, justify="center")
        dish_next = tk.Label(self, text=lunch.dish[1], padding=10, font=main, borderwidth=2, justify="center")
        arrow = tk.Label(self, text='\n→', padding=25, font=main, borderwidth=2)

        empty_label.grid(row=0, column=0, rowspan=2, padx=20)
        date_today.grid(row=0, column=1)
        arrow.grid(rowspan=2, row=0, column=2)
        date_next.grid(row=0, column=3)
        dish_today.grid(row=1, column=1)
        dish_next.grid(row=1, column=3)


