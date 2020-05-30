import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

while True:
    if GPIO.input(4):
        # off
        print("no light")
    else:
        print("light incoming")
