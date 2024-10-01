from gpiozero import Servo
from gpiozero.tools import sin_values
from signal import pause

servo = Servo(17)

# You can use the inbuilt methods
try:
      while True:
           servo.value = -1
           sleep(1)
           servo.value = 0
           sleep(1)
           servo.value = 1
except KeyboardInterrupt:
	print("Program stopped")