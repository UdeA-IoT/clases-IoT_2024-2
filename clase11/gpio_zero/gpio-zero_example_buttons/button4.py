from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(4)

led.source = button

pause()