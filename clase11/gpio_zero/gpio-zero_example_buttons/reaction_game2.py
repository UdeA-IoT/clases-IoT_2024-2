from gpiozero import Button, LED
from time import time, sleep
from random import randint

# Variables
best_time = 1000

# I/O conections
led = LED(17)
btn_reaction = Button(4)
btn_reset = Button(3)

def reset():
    global best_time
    print("Reiniciando juego")
    best_time = 1000

btn_reset.when_pressed = reset

#  test your wiring
while True:
    sleep(randint(1,10))
    led.on()
    start = time()
    btn_reaction.wait_for_press()
    led.off()
    end = time()
    reaction_time = end - start    
    if end - start < best_time:
        best_time = reaction_time
    print(f"Tiempo de reaccion: {reaction_time} - Tiempo a superar: {best_time}")    


