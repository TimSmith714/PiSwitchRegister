import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_DATA = 16 #Pin 36 on GPIO
PIN_LATCH = 20 #Pin 28 on GPIO
PIN_CLOCK = 21 #Pin 40 on GPIO
GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

def shiftout(byte):
        GPIO.output(PIN_LATCH, 0)
        for x in range(8):
                GPIO.output(PIN_DATA, (byte >> x) & 1)
                time.sleep(0.1)
                GPIO.output(PIN_CLOCK, 1)
                time.sleep(0.1)
                GPIO.output(PIN_CLOCK, 0)
                time.sleep(0.1)
        GPIO.output(PIN_LATCH, 1)
    
# Reset all pins
shiftout(0)
shiftout(0)

# Turn on all pins
shiftout(255)
shiftout(256)

