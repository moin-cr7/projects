import pyfirmata
import time
# import serial
import keyboard as key
# ser = serial.Serial("COM9", 38400, timeout = 1)
board = pyfirmata.Arduino('COM5')

# button= board.get_pin('d:2:i')
led=board.get_pin('d:13:o')
value=0
while True:
    # val= ser.readline()
    if(key.is_pressed('o')):
        # print('A')
        # value=1
        led.write(1)
        # time.sleep(1)
    elif( key.is_pressed('f')):
        # value=0
        led.write(0)
        # time.sleep(1)
        # print('a')
    # time.sleep(1)

import Serial
# ser = serial.Serial("COM9", 38400, timeout = 1) #Change your port name COM... and your baudrate
#
# def retrieveData():
#     ser.write(b'1')
#     data = ser.readline().decode('ascii')
#     return data
#
# while(True):
#     uInput = input("Retrieve data? ")
#     if uInput == '1':
#         print(retrieveData())
#     else:
#         ser.write(b'0')