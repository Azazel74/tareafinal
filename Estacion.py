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

