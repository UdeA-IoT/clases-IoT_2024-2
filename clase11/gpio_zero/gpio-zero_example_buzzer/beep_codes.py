
from gpiozero import Buzzer

buzzer = Buzzer(17)

""" 
https://www.pcmag.com/encyclopedia/term/beep-codes
https://blog.adafruit.com/2021/02/19/how-to-use-a-buzzer-to-play-music-with-raspberry-pi-pico-piday-raspberrypi-raspberry_pi/
https://blog.adafruit.com/2021/02/19/how-to-use-a-buzzer-to-play-music-with-raspberry-pi-pico-piday-raspberrypi-raspberry_pi/
https://www.freva.com/buzzer-on-raspberry-pi-generating-beeps/

beep(on_time=1, off_time=1, n=None, background=True)

"""


while True:
    buzzer.beep()
