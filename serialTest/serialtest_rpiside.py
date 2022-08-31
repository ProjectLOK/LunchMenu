import serial

if(serial.inWaiting()>0):
    data = serial.read()