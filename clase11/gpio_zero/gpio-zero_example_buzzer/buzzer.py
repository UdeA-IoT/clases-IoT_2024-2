from gpiozero import Buzzer
from time import sleep

# El buzzer empleado debe ser activo para que pite

""" 
Documentacion: 
https://gpiozero.readthedocs.io/en/stable/api_output.html#buzzer
"""

buzzer = Buzzer(17)

while True:
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    sleep(1)