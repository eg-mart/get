import RPi.GPIO as GPIO
from time import sleep


dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13


def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]


def adc():
    cur = 128
    dac_val = 0
    for i in range(8):
        dac_val += cur
        GPIO.output(dac, decimal2binary(dac_val))
        sleep(0.001)
        if GPIO.input(comp):
            dac_val -= cur
        cur //= 2
    return dac_val


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)


try:
    while (True):
        v = adc()
        num_leds = int(v / 255 * 8)
        GPIO.output(leds, 0)
        GPIO.output(leds[:num_leds], 1)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()