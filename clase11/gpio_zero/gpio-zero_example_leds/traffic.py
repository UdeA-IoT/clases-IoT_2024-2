from gpiozero import LED
from time import sleep

red_led = LED(17)
yel_led = LED(27)

red_led.on()
sleep(1)
yel_led.on()
sleep(1)
red_led.off()
sleep(1)
yel_led.off()

""" 
Challenge time

You have now seen how to add a second LED to your make. I would like to challenge you to do the following independently:

1. Wire and code a third LED into your make.
2. Add code to your program so that the LEDs behave like traffic lights.

Optional: Make a wave of light that travels from the top to the bottom.
"""