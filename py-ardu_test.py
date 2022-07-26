import time

import serial
import asyncio
import aioschedule as sch
import schedule as sc


def get_data():
    ardu.write(str(1).encode('utf-8'))
    ardu.read()


ardu = serial.Serial('/dev/ttyACM0', 9600, timeout= 1)
ardu.reset_input_buffer()
sc.every(30).minute.do(get_data)

while True:
    sc.run_pending()
    time.sleep(1)


