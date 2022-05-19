from scripts.nWeather_api import weather_api
import tkinter as tk
wt = weather_api()
main = ('Arial', 70)
small = ('Arial', 45)

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class WeatherPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.min_today = tk.Label(self, text=wt.min[0], font=small)
        self.max_today = tk.Label(self, text=wt.max[0], font=small)
        self.min_today.grid(column=0, row=0)
        self.max_today.grid(column=0, row=1)
