from gpiozero import LED, Button
from time import sleep

# I/O contections
btn = Button(4)
led = LED(17)

# Functionality
while True:
    if btn.is_pressed:
        print("You pressed me")
        led.on()
        sleep(5)
        led.off()

