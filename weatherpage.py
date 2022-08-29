<<<<<<< Updated upstream
=======
import tkinter as tk
import gviz_api
import gviz_data_table
from scripts.nWeather_api import weather_api

wt = weather_api()
wt.api_call()
main = ('Arial', 70)
small = ('Arial', 45)


class WeatherPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.min_today = tk.Label(self, text=wt.min[0], font=small)
        self.max_today = tk.Label(self, text=wt.max[0], font=small)
        self.min_today.grid(column=0, row=0)
        self.max_today.grid(column=0, row=1)
>>>>>>> Stashed changes
