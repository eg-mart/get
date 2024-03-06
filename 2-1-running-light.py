import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

for i in range(8): GPIO.setup(leds[i], GPIO.OUT)
for i in range(8): GPIO.output(leds[i], 0)

for i in range(8): GPIO.setup(aux[i], GPIO.IN)

while(True):
    for i in range(8): GPIO.output(leds[i], GPIO.input(aux[i]))
