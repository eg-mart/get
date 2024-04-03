import RPi.GPIO as GPIO
from time import sleep


dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13


def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]


def adc():
    dac_val = 0
    GPIO.output(dac, 0)
    sleep(0.001)
    comp_res = GPIO.input(comp)
    while (not comp_res and dac_val < 255):
        dac_val += 1
        GPIO.output(dac, 0)
        GPIO.output(dac, decimal2binary(dac_val))
        sleep(0.001)
        comp_res = GPIO.input(comp)
        GPIO.output(dac, 0)
    return dac_val


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)


try:
    while (True):
        v = adc()
        print(f"adc: {v}, voltage: {v / 255 * 3.3}")
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()