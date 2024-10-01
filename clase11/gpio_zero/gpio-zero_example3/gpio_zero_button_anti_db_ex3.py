from gpiozero import Button

buttonPin = Button(17, bounce_time=0.2) 
while True:
    if buttonPin.is_pressed:
        print("Boton presionado")
