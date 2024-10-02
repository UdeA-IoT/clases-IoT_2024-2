from gpiozero import Buzzer
from time import sleep

# El buzzer empleado debe ser activo para que pite


buzzer = Buzzer(17)

while True:
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    sleep(1)