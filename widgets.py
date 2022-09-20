import json
import tkinter as tk
import re
import tkinter.font
import schedule as sch
import asyncio
import scripts.lunch_api as lunch_api
import time

placeholder = None

with open('config.json', 'r') as data:
    config = data.read()
    data.close()
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
        self.dish =             tk.StringVar()
        self.cal =              tk.StringVar()
        update_loop =           asyncio.create_task(self.update())

        font_title =            pack_font(fonts[class_name(self)]['title'])
        font_dish =             pack_font(fonts[class_name(self)]['dish'])
        font_cal =              pack_font(fonts[class_name(self)]['cal'])

        title =                 tk.Label(self,          text='오늘 급식',               font=font_title)
        dish_label =            tk.Label(self,          textvariable=self.dish,         font=font_dish)
        cal_label =             tk.Label(self,          textvariable=self.cal,          font=font_cal)

        title.                  grid(row=0, column=0)
        dish_label.             grid(row=1, column=0)
        cal_label.              grid(row=2, column=0)

    async def update(self):
        while True:
            self.dish.set(lunch_data.dish[0])
            self.cal.set(lunch_data.cal[0])
            await asyncio.sleep(0.01)

class NextdayLunch(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(NextdayLunch, self).__init__(parent, *args, **kwargs)
        self.dish =             tk.StringVar()
        self.cal =              tk.StringVar()
        update_loop =           asyncio.create_task(self.update())

        dish_font =             pack_font(fonts[class_name(self)]['dish'])
        cal_font =              pack_font(fonts[class_name(self)]['cal'])

        dish_label =            tk.Label(self,          textvariable=self.dish,         font=dish_font)
        cal_label =             tk.Label(self,          textvariable=self.cal,          font=cal_font)

        dish_label.             grid(row=0, column=0)
        cal_label.              grid(row=1, column=0)

    async def update(self):
        while True:
            self.dish.set(lunch_data.dish[1])
            self.cal.set(lunch_data.cal[1])
            await asyncio.sleep(0.01)

class Sensor(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Sensor, self).__init__(parent, *args, **kwargs)
        self.temperature =      tk.StringVar()
        self.humidity =         tk.StringVar()
        self.fine =             tk.StringVar()
        self.ultrafine =        tk.StringVar()
        self.co2 =              tk.StringVar()
        update_loop =           asyncio.create_task(self.update())

        category_font =         pack_font(fonts[class_name(self)]["category"])
        unit_font =             pack_font(fonts[class_name(self)]["unit"])
        data_font =             pack_font(fonts[class_name(self)]["data"])

        frame_air =             tk.Frame(self)

        category_air =          tk.Label(frame_air,     text="온습도",                  font=category_font,     justify=tk.LEFT)
        data_temperature =      tk.Label(frame_air,     textvariable=self.temperature,  font=data_font)
        unit_celcius =          tk.Label(frame_air,     text="°C",                      font=unit_font)
        split_bar =             tk.Label(frame_air,     text="|",                       font=category_font)
        data_humidity =         tk.Label(frame_air,     textvariable=self.humidity,     font=data_font)
        not_unit_percent =      tk.Label(frame_air,     text="%",                       font=unit_font)

        category_air.           grid(row=0, column=0, columnspan=5)
        data_temperature.       grid(row=1, column=0)
        unit_celcius.           grid(row=1, column=1)
        split_bar.              grid(row=1, column=2)
        data_humidity.          grid(row=1, column=3)
        not_unit_percent.       grid(row=1, column=4)

        category_fine =         tk.Label(self,          text="미세먼지",                font=category_font,     justify=tk.LEFT)
        unit_fine =             tk.Label(self,          text="μg/m³",                   font=unit_font,         justify=tk.RIGHT)
        data_fine =             tk.Label(self,          textvariable=self.fine,         font=data_font,         justify=tk.LEFT)
        lamp_fine =             placeholder
        category_ultrafine =    tk.Label(self,          text="초미세먼지",              font=category_font,     justify=tk.LEFT)
        unit_ultrafine =        tk.Label(self,          text="μg/m³",                   font=unit_font,         justify=tk.RIGHT)
        data_ultrafine =        tk.Label(self,          textvariable=self.ultrafine,    font=data_font,         justify=tk.LEFT)
        lamp_ultrafine =        placeholder
        category_co2 =          tk.Label(self,          text="이산화탄소",              font=category_font,     justify=tk.LEFT)
        unit_co2 =              tk.Label(self,          text="ppm",                     font=unit_font,         justify=tk.RIGHT)
        data_co2 =              tk.Label(self,          textvariable=self.co2,          font=data_font,         justify=tk.LEFT)
        lamp_co2 =              placeholder

        frame_air.              grid(row=0, column=0, columnspan=3)
        category_fine.          grid(row=1, column=0, columnspan=2)
        unit_fine.              grid(row=2, column=0)
        data_fine.              grid(row=2, column=1)
        lamp_fine
        category_ultrafine.     grid(row=3, column=0, columnspan=2)
        unit_ultrafine.         grid(row=4, column=0)
        data_ultrafine.         grid(row=4, column=1)
        lamp_ultrafine
        category_co2.           grid(row=5, column=0, columnspan=2)
        unit_co2.               grid(row=6, column=0)
        data_co2.               grid(row=6, column=1)
        lamp_co2

    async def update(self):
        while True:
            self.temperature.set("27")
            self.humidity.set("63")
            self.fine.set("10")
            self.ultrafine.set("100")
            self.co2.set("20")
            await asyncio.sleep(0.01)

class Clock(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Clock, self).__init__(parent, *args, **kwargs)
        self.date =             tk.StringVar()
        self.time =             tk.StringVar()
        clock_loop =            asyncio.create_task(self.update())

        font_date = pack_font(fonts[class_name(self)]['date'])
        font_time = pack_font(fonts[class_name(self)]['time'])

        date_label =            tk.Label(self,          textvariable=self.date,         font=font_date)
        time_label =            tk.Label(self,          textvariable=self.time,         font=font_time)

        date_label.             grid(row=0, column=0)
        time_label.             grid(row=1, column=0)
        
    async def update(self):
        while True:
            self.date.set(time.strftime("%m{} %d{} {}{}").format("월", "일", "일월화수목금토"[int(time.strftime("%w"))], "요일"))
            self.time.set(time.strftime("%I:%M"))
            await asyncio.sleep(0.01)
