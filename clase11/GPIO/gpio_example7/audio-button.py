# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

# Archivo tomado y adaptaado de: https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/bread-board-setup-for-input-buttons
 
import time
import os

# Pins definitions
button1 = 23
button2 = 24
button3 = 25

print("press a button!")

# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
try:
  while True:
    # omxplayer -o local <file>
    # omxplayer -o hdmi <file>
    # omxplayer -o both <file>

    if not GPIO.input(button1):
      os.system('omxplayer temple-bell.mp3 &')
    if not GPIO.input(button2):
      os.system('omxplayer temple-bell-bigger.mp3 &')
    if not GPIO.input(button3):
      os.system('omxplayer temple-bell-huge.mp3 &') 
    time.sleep(.25)
# When you press ctrl+c, this will be called
finally:
  GPIO.cleanup()




 

