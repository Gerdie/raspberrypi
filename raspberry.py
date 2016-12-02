#raspberry pi and wemos-d1-mini ESP8266 with micropython (wifi built-in)

#to connect to raspberrypi, component must operate at 3.3 volts (not 5 volts)
#components must be digital - raspberrypi can't measure voltage. no state-change thermometers
#unless you have analog to digital converter...

#using maxim/dallas DS18B20 temp sensor that has serial protocol

#breadboard = prototyping board. connected to raspberrypi pins via wires.
#4.7k resistor

#SD cards can handle limited amt of rewrites --> use Redis not sqlite
#with Redis if power goes out you can lose data

#pip intall redislite

from redislite import StrictRedis
from redis_collections import List


def read_temp_celsius():
    with open('file/to/driver/w1_slave') as device:
        for line in device:
            value = line.strip().split()[-1]
            if value.startswith('t='):
                return float(value[2:])/1000.0

redis_connection = StrictRedis('')
