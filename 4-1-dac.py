import RPi.GPIO as GPIO


def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]


GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        try:
            num = int(input("Type a number from 0 to 255: "))
            if 0 <= num <= 255:
                GPIO.output(dac, decimal2binary(num))
                voltage = float(num) / 256.0 * 3.3
                print(f"Expected voltage: {voltage:.4} volts")
            else:
                if num < 0:
                    print("Number have to be >=0! Try again")
                elif num > 255:
                    print("Number is out of range [0,255]! Try again")  
        except Exception as e:
            print(e)
            if num == "q": break
            print("Error: input isn't a number. Try again")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    