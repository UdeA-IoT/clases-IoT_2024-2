from gpiozero import LED
from time import sleep

red_led = LED(17)

""" 
Ensayar comando por comando en la terminal de python

Documentacion: https://gpiozero.readthedocs.io/en/stable/api_output.html#led


"""

red_led.blink(0.1, 0.2)
# red_led.blink(0.2, 0.1, 5)
# red_led.toggle()
# sleep(1)
# print(red_led.is_lit)
# red_led.toggle()
# sleep(1)
# print(red_led.is_lit)