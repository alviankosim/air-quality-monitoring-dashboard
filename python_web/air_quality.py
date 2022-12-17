from serial import Serial
from mysql_connection import *
import time

def arduinoInitialization():
    port = '/dev/cu.usbserial-1130'
    baudRateVal = 9600

    serialArduino = Serial(port, baudRateVal)

    while True:
        while (serialArduino.inWaiting() == 0):
            pass
        valueRead = serialArduino.readline()

        parsedValueRead = valueRead.strip().decode( "utf-8" )
        print(parsedValueRead)
        dbinsertmonitoring(parsedValueRead)
        time.sleep(3) # 3seconds before go through the next loop

arduinoInitialization()