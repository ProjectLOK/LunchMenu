import serial
import time
import json

with open('config.json', 'r') as data:
    config = data.read()
    data.close()
    config = json.loads(config)
    rtSensor = config['sensor']
if rtSensor:
    ardu = serial.Serial("/dev/ttyUSB0", 115200)
    time.sleep(5)

    category = ['temp', 'humi', 'pm10', 'pm2.5', 'co2', 'form']


    def getData():
        dataset = [''] * 6
        ardu.write(str.encode('update'))
        # time.sleep(0.1)
        for i in range(5):
            #print(i)
            data = ardu.readline()  # read until ('\n')
            dataset[i] = data.decode('utf-8').rstrip()
        sensor = dict(zip(category, dataset))
        #print(sensor)
        #print(dataset)
        return sensor


    getData()
    time.sleep(1)
    getData()
