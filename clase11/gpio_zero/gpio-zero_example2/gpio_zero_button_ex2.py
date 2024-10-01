from gpiozero import Button

buttonPin = Button(17) # No fue necesario  la resistencia de pull-up

while True:
    if buttonPin.is_pressed:
        print("Boton presionado")

