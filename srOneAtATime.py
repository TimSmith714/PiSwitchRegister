import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
PIN_DATA = 16
PIN_LATCH = 20
PIN_CLOCK = 21
gpio.setup(PIN_DATA, gpio.OUT)
gpio.setup(PIN_LATCH, gpio.OUT)
gpio.setup(PIN_CLOCK, gpio.OUT)

def shiftout(byte):
    gpio.output(PIN_LATCH, 0)
    for x in range(8):
        gpio.output(PIN_DATA, (byte >> x) & 1)
        gpio.output(PIN_CLOCK, 1)
        gpio.output(PIN_CLOCK, 0)
    gpio.output(PIN_LATCH, 1)

for i in range(8):
    shiftout(2**i)
    time.sleep(0.2)


