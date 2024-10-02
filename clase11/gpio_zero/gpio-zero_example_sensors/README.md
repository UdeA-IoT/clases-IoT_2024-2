# Sensores

Cosas tomadas de la pagina de rPi.

* https://trinket.io/sense-hat
* https://www.raspberrypi.org/blog/desktop-sense-hat-emulator/
* https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/2
* https://trinket.io/sense-hat

## Setting up

You have completed a number of computing projects now, so I will leave some of the details to you. As a reminder, here are the steps you need to take to set up the sensor in your program:
* To interact with a component, you have to import a class from the GPIO Zero library
* To use the class you must create an object, store it in a variable, and provide a GPIO pin for the specific component

## Sense hat


Ejemplo 1: https://trinket.io/python/667839c0c4

```python
from sense_hat import SenseHat
import time

sense = SenseHat()

temperature = round(sense.temperature, 1)
sense.show_message("It is " + str(temperature) + " degrees")
```

Ejemplo 2: https://trinket.io/python/9dbff599d9

```python
from sense_hat import SenseHat
import time

sense = SenseHat()

temperature = round(sense.temperature, 1)
sense.show_message("It is " + str(temperature) + " degrees")

pressure = round(sense.pressure, 1)
sense.show_message("It is " + str(pressure) + " hPa")
```

Ejemplo 3: https://trinket.io/python/7c798bd6b2


```python
from sense_hat import SenseHat
import time

sense = SenseHat()

temperature = round(sense.temperature, 1)

if temperature > 25 and temperature < 35:
    sense.show_message("That's quite warm")

elif temperature > 10 and temperature <= 25:
    sense.show_message("Not too cold")

elif temperature > -15 and temperature <= 10:
    sense.show_message("Brr, it's chilly")

elif temperature >= 100:
    sense.show_message("It's boiling")

elif temperature >= 35 or temperature <= -15:
    sense.show_message("The temperature is extreme!")
```

Ejemplo 4 - Make an outfit recommender: https://trinket.io/python/cca7dc0dd1

Create a program using the Sense HAT emulator that suggests an outfit depending on the temperature and humidity.

Your program should suggest:

* A thick winter jacket when the temperature is under 10°C and the humidity is over 35%
* A hat when the temperature is at least 22°C OR the humidity is over 40%

What other outfit suggestions could your program make?


```python
from sense_hat import SenseHat
import time

sense = SenseHat()


while True: 
  temperature = round(sense.temperature, 1)
  humidity = round(sense.humidity, 1)

  if temperature < 25 and humidity > 35:
    sense.show_message("You need a thick winter jacket")
  elif temperature >= 22 or humidity >= 40:
    sense.show_message("You need a hat")
```

## Camara:

* https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/2
* https://sense-emu.readthedocs.io/en/v1.1/#
* https://www.raspberrypi.com/news/sense-hat-emulator/
* https://www.raspberrypi.org/blog/desktop-sense-hat-emulator/
* https://atareao.es/tutorial/raspberry-pi-400/sense-hat-emulator/
* https://www.raspberrypi.com/news/a-hedgehog-cam-or-two/
* https://iancarpenter.dev/2016/08/28/a-step-by-step-guide-to-building-a-raspberry-pi-hedgehog-camera/
* https://blog.adafruit.com/2022/12/15/outdoor-case-raspberry-pi-zero-for-hedgehog-house-3dthursday-3dprinting/
* https://makezine.com/article/craft/photography-video/spy-on-garden-critters-with-raspberry-pi-powered-night-vision/
* https://www-users.york.ac.uk/~mjf5/hedgehog_camera/index.html





