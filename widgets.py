import json
import tkinter as tk
import re
import tkinter.font
import schedule as sch
import asyncio
import scripts.lunch_api as lunch_api
import time

with open('config.json', 'r') as config:
    config = config.read()
    config = json.loads(config)
    fonts = config['fonts']

def class_name(self):
    return re.sub(r'[.!]+', '', str(self))

def pack_font(data):
    return tk.font.Font(**data)

class LunchData:
    def __init__(self):
        self.data = lunch_api.lunch_api()
        self.data.api_call()
        self.dish = self.data.dish
        self.cal = self.data.cal
        sch.every().day.at("03:00").do(self.update)

    def update(self):
        self.data.api_call()
lunch_data = LunchData()
        

class TodayLunch(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(TodayLunch, self).__init__(parent, *args, **kwargs)
        self.dish = tk.StringVar()
        self.cal = tk.StringVar()
        update_loop = asyncio.create_task(self.update())

        title = tk.Label(self, text='오늘 급식', font= pack_font(fonts[class_name(self)]['title']))
        dish_label = tk.Label(self, textvariable=self.dish, font=pack_font(fonts[class_name(self)]['dish']))
        cal_label = tk.Label(self, textvariable=self.cal, font=pack_font(fonts[class_name(self)]['cal']))

        title.grid(row=0, column=0)
        dish_label.grid(row=1, column=0)
        cal_label.grid(row=2, column=0)

    async def update(self):
        while True:
            self.dish.set(lunch_data.dish[0])
            self.cal.set(lunch_data.cal[0])
            await asyncio.sleep(0.01)


class NextdayLunch(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(NextdayLunch, self).__init__(parent, *args, **kwargs)
        self.dish = tk.StringVar()
        self.cal = tk.StringVar()
        update_loop = asyncio.create_task(self.update())

        dish_label = tk.Label(self, textvariable=self.dish, font=pack_font(fonts[class_name(self)]['dish']))
        cal_label = tk.Label(self, textvariable=self.cal, font=pack_font(fonts[class_name(self)]['cal']))

        dish_label.grid(row=0, column=0)
        cal_label.grid(row=1, column=0)

    async def update(self):
        while True:
            self.dish.set(lunch_data.dish[1])
            self.cal.set(lunch_data.cal[1])
            await asyncio.sleep(0.01)



class Clock(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Clock, self).__init__(parent, *args, **kwargs)
        self.date, self.time = tk.StringVar(), tk.StringVar()
        clock_loop = asyncio.create_task(self.update())

        date_label = tk.Label(self, textvariable=self.date, font=pack_font(fonts[class_name(self)]['date']))
        time_label = tk.Label(self, textvariable=self.time, font=pack_font(fonts[class_name(self)]['time']))

        date_label.grid(row=0, column=0)
        time_label.grid(row=1, column=0)
        
    async def update(self):
        while True:
            self.date.set(time.strftime("%m{} %d{} {}{}").format("월", "일", "일월화수목금토"[int(time.strftime("%w"))], "요일"))
            self.time.set(time.strftime("%I:%M"))
            await asyncio.sleep(0.01)
