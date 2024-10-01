import RPi.GPIO as GPIO
import time

# Pin Definitons
buttonPin = 17

# Pin Setup
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme GPIO.setup(buttonPin,GPIO.IN) # LED pin set as output
try:
    while True:
        buttonValue = GPIO.input(buttonPin)
        if buttonValue == True:
            print("Boton presionado")
        time.sleep(0.2)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly: 
    GPIO.cleanup() # cleanup all GPIO 