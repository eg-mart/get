import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(8): GPIO.setup(dac[i], GPIO.OUT)
for i in range(8): GPIO.output(dac[i], number[i])

time.sleep(12.5)

for i in range(8): GPIO.output(dac[i], 0)


##voltage_values = [3.24, 1.67, 0.87, 0.46, 0.11, 0]
GPIO.cleanup()