from gpiozero import Button, LED

btn = Button(4)
led = LED(17)

# En este caso se usan eventos
btn.when_pressed = led.on

btn.when_released = led.off

