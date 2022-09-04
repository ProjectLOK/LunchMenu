import serial

ardu = serial.Serial("/dev/ttyUSB0", 115200)
while True:
    data = ardu.read()
    print(data)


if(serial.inWaiting()>0):
    data = serial.read()
    dataset = ['']*5
    return dataset