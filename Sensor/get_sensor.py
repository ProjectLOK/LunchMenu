import serial
import time

ardu = serial.Serial("/dev/ttyUSB0", 115200)
time.sleep(5)  #give some time for initialize

category = ['temp', 'humi', 'pm10', 'pm2.5', 'co2', 'form']

def getData():
    dataset = [''] * 6
    ardu.write(str.encode('update'))
    if serial.inWaiting:
        for i in range(6):
            data = ardu.readline()      #read until ('\n')
            dataset[i] = data.decode('utf-8').rstrip()
        sensor = dict(zip(category, dataset))
        return sensor

