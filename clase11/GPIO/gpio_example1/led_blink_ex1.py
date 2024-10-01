import RPi.GPIO as GPIO
import time

# Pin Definitons
ledPin = 18

# Pin Setup
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme GPIO.setup(ledPin,GPIO.OUT) # LED pin set as output
try:
    while True:
        GPIO.output(ledPin, True)
        time.sleep(1) 
        GPIO.output(ledPin, False)
        time.sleep(1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly: 
    GPIO.cleanup() # cleanup all GPIO 

