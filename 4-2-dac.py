def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]


import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

period = int(input("Enter signal period: "))
voltage = 0
delta = 1

try:
    while(True):
        time.sleep(period / 256 / 2)
        voltage += delta
        GPIO.output(dac, decimal2binary(voltage))

        if voltage >= 255:
            delta = -1
        elif voltage <= 0:
            delta = 1
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    