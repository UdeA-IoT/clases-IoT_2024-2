from gpiozero import Button
from time import sleep

# I/O contections
btn = Button(4)

# Functionality
while True:
    if btn.is_pressed:
        print("You pressed me")
    sleep(0.1)

