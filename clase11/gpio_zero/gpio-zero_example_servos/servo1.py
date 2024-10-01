from gpiozero import Servo
from time import sleep

servo = Servo(17)

# You can use the inbuilt methods
try:
      while True:
           servo.min()
           sleep(1)
           servo.mid()
           sleep(1)
           servo.max()
except KeyboardInterrupt:
	print("Program stopped")