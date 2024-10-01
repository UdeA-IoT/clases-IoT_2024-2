from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(4)

while True:
    button.wait_for_press()
    led.toggle()
    sleep(0.5)