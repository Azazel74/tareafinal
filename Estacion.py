from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import time
import grovepi
import datetime as dt
import csv

#Temperatura y humedad
dht_sensor_port = 3
dht_sensor_type = 0

#intensidad luminica
light_sensor = 0

#Potenciometro
potentiometer = 2

min_sampling_time = 1
max_sampling_time = 5

def sampling_time():
    i = grovepi.analogRead(potentiometer)
    sampling_time = min_sampling_time + (float(i) / 1023) * (max_sampling_time - min_sampling_time)
    return sampling_time

log_file = "/home/pi/Desktop/Datos1.csv"

#LCD
setRGB(128,128,128)

while True:
    try:
     
        #Temperatura y humedad
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        print("temp =", temp, "C\thumidity =", hum,"%")
        
        if isnan(temp) is True or isnan(hum) is True:
            raise TypeError('nan error')

        t = str(temp)
        h = str(hum)
        
        #Intensidad luminica
        sensor_value = grovepi.analogRead(light_sensor)
        s = str(sensor_value)
        
        resistance = (float)(1023 - sensor_value) * 68 / sensor_value
        r = str(resistance)

        print("sensor_value = %d resistance =%.2f" % (sensor_value,  resistance))
       # time.sleep(.5)
