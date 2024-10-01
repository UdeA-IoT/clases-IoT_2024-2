from gpiozero import Button, LED
from time import time, sleep
from random import randint

# I/O conections
led = LED(17)
btn = Button(4)

#  test your wiring
while True:
    sleep(randint(1,10))
    led.on()
    start = time()
    btn.wait_for_press()
    led.off()
    end = time()
    print(end - start)
