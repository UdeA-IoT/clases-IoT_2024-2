from gpiozero import LED
from time import sleep

red_led = LED(17)
yel_led = LED(27)

while True:
    red_led.on()
    sleep(1)
    yel_led.on()
    sleep(1)
    red_led.off()
    sleep(1)
    yel_led.off()
