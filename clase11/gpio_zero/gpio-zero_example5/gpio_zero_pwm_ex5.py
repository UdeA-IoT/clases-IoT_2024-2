from gpiozero import PWMLED

led_pin = PWMLED(18)
while True:
    duty_s = input("Enter Brightness (0 to 100): ")
    duty = int(duty_s)/100
    led_pin.value = duty
