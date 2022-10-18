import json
import tkinter as tk
import re
import tkinter.font
import schedule as sch
import asyncio
import scripts.lunch_api as lunch_api
import time
import scripts.Sensor.get_sensor_for_debug as ardu_sensor

placeholder = None

with open('config.json', 'r') as data:
    config = data.read()
    data.close()
    config = json.loads(config)
    fonts = config['fonts']
    rtSensor = config['sensor']



with open('presets/main.json', 'r') as data:
    preset_main = json.loads(data.read())["composition"]
    data.close()

def class_name(self):
    return re.sub(r'[.!]+', '', str(self))

def pack_font(data):
    if "weight" in data.keys():
        data["weight"] = getattr(tk.font, data["weight"])
    if "slant" in data.keys():
        data["slant"] = getattr(tk.font, data["slant"])
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
        self.grid_propagate(0)
        self.pack_propagate(0)
        self.title = tk.StringVar()
        self.title.set('오늘 급식')
        self.dish =             tk.StringVar()
        self.cal =              tk.StringVar()
        sch.every().monday.at("12:10").do(lambda: self.dish.set(lunch_data.dish[1]))
        sch.every().tuesday.at("12:10").do(lambda: self.dish.set(lunch_data.dish[1]))
        sch.every().wednesday.at("12:10").do(lambda: self.dish.set(lunch_data.dish[1]))
        sch.every().thursday.at("12:10").do(lambda: self.dish.set(lunch_data.dish[1]))
        sch.every().friday.at("12:10").do(lambda: self.dish.set(lunch_data.dish[1]))
        sch.every().day.at("12:10").do(lambda: self.title.set('내일 급식'))
        sch.every().day.at("00:01").do(lambda: self.title.set('오늘 급식'))
        sch.every().monday.at("03:01").do(lambda: self.dish.set(lunch_data.dish[0]))
        sch.every().tuesday.at("03:01").do(lambda: self.dish.set(lunch_data.dish[0]))
        sch.every().wednesday.at("03:01").do(lambda: self.dish.set(lunch_data.dish[0]))
        sch.every().thursday.at("03:01").do(lambda: self.dish.set(lunch_data.dish[0]))
        sch.every().friday.at("03:01").do(lambda: self.dish.set(lunch_data.dish[0]))
        update_loop =           asyncio.create_task(self.update())

        font_title =            pack_font(fonts[class_name(self)]['title'])
        font_dish =             pack_font(fonts[class_name(self)]['dish'])
        font_cal =              pack_font(fonts[class_name(self)]['cal'])

        title_label =                 tk.Label(self,          textvariable=self.title,               font=font_title,                        relief='solid',     bd=0, bg='white')
        dish_label =            tk.Label(self,          textvariable=self.dish,         font=font_dish,    anchor='center',     relief='solid',     bd=0, bg='white')
        cal_label =             tk.Label(self,          textvariable=self.cal,          font=font_cal,     anchor='center',     relief='solid',     bd=0, bg='white')

        title_label.                  grid(row=0, column=0, ipadx=298)
        dish_label.             grid(row=1, column=0)
        cal_label.              grid(row=2, column=0)
        self.                   config(relief='solid', bd=10, bg='white')

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

        dish_label =            tk.Label(self,          textvariable=self.dish,         font=dish_font, anchor='center', bg='white')
        cal_label =             tk.Label(self,          textvariable=self.cal,          font=cal_font, anchor='center', bg='white')

        dish_label.             grid(row=0, column=0, sticky='nsew', ipadx='40')
        cal_label.              grid(row=1, column=0)
        self.config(relief='solid', bd=10, bg='white')

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

        category_font =         pack_font(fonts[class_name(self)]["category"])
        unit_font =             pack_font(fonts[class_name(self)]["unit"])
        data_font =             pack_font(fonts[class_name(self)]["data"])

        frame_air =             tk.Frame(self)
        frame_air.config(bg='white')

        category_air =          tk.Label(frame_air,     text="AIR",                  font=category_font,     justify=tk.LEFT, anchor='w', bg='white',     relief='solid',     bd=0)
        data_temperature =      tk.Label(frame_air,     textvariable=self.temperature,  font=data_font, bg='white',     relief='solid',     bd=0)
        unit_celcius =          tk.Label(frame_air,     text="°C",                      font=unit_font, bg='white',     relief='solid',     bd=0)
        split_bar =             tk.Label(frame_air,     text="|",                       font=category_font, bg='white',     relief='solid',     bd=0)
        data_humidity =         tk.Label(frame_air,     textvariable=self.humidity,     font=data_font, bg='white',     relief='solid',     bd=0)
        not_unit_percent =      tk.Label(frame_air,     text="%",                       font=unit_font, bg='white',     relief='solid',     bd=0)
        line = tk.Label(self, bg='black', height='1')

        category_air.           grid(row=0, column=0, columnspan=5, sticky='w')
        data_temperature.       grid(row=1, column=0)
        unit_celcius.           grid(row=1, column=1)
        split_bar.              grid(row=1, column=2)
        data_humidity.          grid(row=1, column=3)
        not_unit_percent.       grid(row=1, column=4)

        category_fine =         tk.Label(self,          text="PM 10",                font=category_font,     justify=tk.LEFT, anchor='w', bg='white')
        unit_fine =             tk.Label(self,          text="μg/m³",                   font=unit_font,         justify=tk.RIGHT, bg='white')
        data_fine =             tk.Label(self,          textvariable=self.fine,         font=data_font,         justify=tk.LEFT, bg='white')
        lamp_fine =             placeholder
        category_ultrafine =    tk.Label(self,          text="PM 2.5",              font=category_font,     justify=tk.LEFT, bg='white')
        unit_ultrafine =        tk.Label(self,          text="μg/m³",                   font=unit_font,         justify=tk.RIGHT, bg='white')
        data_ultrafine =        tk.Label(self,          textvariable=self.ultrafine,    font=data_font,         justify=tk.LEFT, bg='white')
        lamp_ultrafine =        placeholder
        category_co2 =          tk.Label(self,          text="CO₂",              font=category_font,     justify=tk.LEFT, bg='white')
        unit_co2 =              tk.Label(self,          text="ppm",                     font=unit_font,         justify=tk.RIGHT, bg='white')
        data_co2 =              tk.Label(self,          textvariable=self.co2,          font=data_font,         justify=tk.LEFT, bg='white')
        lamp_co2 =              placeholder

        frame_air.              grid(row=0, column=0, columnspan=3)
        #line.grid(row=1, column=0, columnspan=3, sticky='nsew')
        category_fine.          grid(row=2, column=0, columnspan=2, sticky='w')
        data_fine.              grid(row=3, column=0, sticky='w')
        unit_fine.              grid(row=3, column=1, sticky='w')
        lamp_fine
        category_ultrafine.     grid(row=4, column=0, columnspan=2, sticky='w')
        data_ultrafine.         grid(row=5, column=0, sticky='w')
        unit_ultrafine.         grid(row=5, column=1, sticky='w')

        lamp_ultrafine
        category_co2.           grid(row=6, column=0, columnspan=2, sticky='w')
        data_co2.               grid(row=7, column=0, sticky='w')
        unit_co2.               grid(row=7, column=1, sticky='w')
        lamp_co2
        
        self.update()
        self.config(bg='white')
        if rtSensor:
            update_loop = asyncio.create_task(self.sche())
            sch.every(1).minute.do(self.update)
            sch.every().monday.at("08:40").do(self.wakeUp)
            sch.every().monday.at("22:00").do(self.sleep)
            sch.every().tuesday.at("08:40").do(self.wakeUp)
            sch.every().tuesday.at("22:00").do(self.sleep)
            sch.every().wednesday.at("08:40").do(self.wakeUp)
            sch.every().wednesday.at("22:00").do(self.sleep)
            sch.every().thursday.at("08:40").do(self.wakeUp)
            sch.every().thursday.at("22:00").do(self.sleep)
            sch.every().friday.at("08:40").do(self.wakeUp)
            sch.every().friday.at("22:00").do(self.sleep)


    def update(self):
        if rtSensor:
            data = ardu_sensor.getData()
            print(data)
            print('sensor updated!')
            data['temp'] = round(float(data['temp']), 1)
            data['humi'] = round(float(data['humi']), 1)
            self.temperature.set(data['temp'])
            self.humidity.set(data['humi'])
            self.fine.set(data['pm10'])
            self.ultrafine.set(data['pm2.5'])
            self.co2.set(data['co2'])
        else:
            self.temperature.set('21')
            self.humidity.set('53')
            self.fine.set('15')
            self.ultrafine.set('20')
            self.co2.set('421')

    if rtSensor:
        async def sche(self):
            while True:
                sch.run_pending()
                await asyncio.sleep(10)


        def sleep(self):
            ardu_sensor.sleep()

        def wakeUp(self):
            ardu_sensor.wake()
    
class Clock(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Clock, self).__init__(parent, *args, **kwargs)
        self.date =             tk.StringVar()
        self.time =             tk.StringVar()
        clock_loop =            asyncio.create_task(self.update())

        font_date = pack_font(fonts[class_name(self)]['date'])
        font_time = pack_font(fonts[class_name(self)]['time'])

        date_label =            tk.Label(self,          textvariable=self.date,         font=font_date, anchor='center', padx= 186, relief='solid', bd=0, bg='white')
        time_label =            tk.Label(self,          textvariable=self.time,         font=font_time, anchor='center', relief='solid', bd=0, bg='white')

        date_label.             grid(row=0)
        time_label.             grid(row=1)
        self.config(relief='solid', bd=10, bg='white')
        
    async def update(self):
        while True:
            self.date.set(time.strftime("%m{} %d{} {}{}").format("월", "일", "일월화수목금토"[int(time.strftime("%w"))], "요일"))
            self.time.set(time.strftime("%I:%M"))
            await asyncio.sleep(0.01)
