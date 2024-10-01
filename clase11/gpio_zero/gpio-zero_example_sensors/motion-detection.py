from gpiozero import MotionSensor, Buzzer
from time import sleep

pir = MotionSensor(4)
buz = Buzzer(17)

while True:
    print(pir.motion_detected)
    sleep(1)
