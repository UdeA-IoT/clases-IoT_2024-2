from gpiozero import MotionSensor, Buzzer
from time import sleep

pir = MotionSensor(4)
buz = Buzzer(17)

while True:
    pir.wait_for_motion()     # will pause the program until motion is detected
    print("Motion detected")
    sleep(1)
