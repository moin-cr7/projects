
import serial

ser = serial.Serial("COM9", 38400, timeout = 1) #Change your port name COM... and your baudrate

def retrieveData():
    ser.write(b'1')
    data = ser.readline().decode('ascii')
    # print(data)
    return data

while(True):
    uInput = input("Retrieve data? ")
    if uInput == '1':
        print(retrieveData())
    else:
        ser.write(b'0')
# import pyfirmata
# import keyboard as key
# import time
# board = pyfirmata.Arduino('com5')
# data=0
# led = board.get_pin('d:13:o')
#
# while True:
#     if(key.is_pressed("o")):
#         led.write(1)
#         # time.sleep(1)
#     elif(key.is_pressed("f")):
#         led.write(0)
        # time.sleep(1)