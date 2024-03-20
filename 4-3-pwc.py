import RPi.GPIO as GPIO


GPIO.setwarnings(False)

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

pin_pwm = GPIO.PWM(pin, 1000)
pin_pwm.start(0)

try:
    while(True):
        k = int(input("Input the duty cycle: "))
        pin_pwm.stop()
        pin_pwm.start(k)
finally:
    pin_pwm.stop()
    GPIO.output(pin, 0)
    GPIO.cleanup()
    