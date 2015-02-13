import laser as laser
import serial
import os
import string
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 115200)
sleep(2)
ser.flushInput()
ser.write('givepos')
output = ser.read(40)
print len ( output) 


