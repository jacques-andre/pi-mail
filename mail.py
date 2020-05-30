import RPi.GPIO as GPIO
from pushover import init, Client
import time

# Pushover
init("<my key>")


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

while True:
    if not GPIO.input(4):
        # on
        Client("<username key>").send_message(
            "Mailbox has been opened", title="You've got mail!"
        )
        time.sleep(120)
