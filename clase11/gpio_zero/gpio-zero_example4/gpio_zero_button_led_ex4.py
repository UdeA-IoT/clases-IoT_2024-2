from gpiozero import Button, LED

switch_pin = Button(18, bounce_time=0.2) 
ledPin = LED(23)
ledPin.off()

led_state = False
old_input_state = True 

while True:
    new_input_state = switch_pin.is_pressed
    if new_input_state == False and old_input_state == True:
        led_state = not led_state
        old_input_state = new_input_state
    ledPin.toggle()
       

