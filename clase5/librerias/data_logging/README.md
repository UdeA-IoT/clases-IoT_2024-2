# Data logging

## Resumen

El **Data logging** es proceso de recolectar y almacenar datos durante un intervalo de tiempo en diferentes sistemas o entornos.

Cuando un dispositivo electronico tiene la capacidad de registrar datos decimos que es un **data logger**. Hay una gran cantidad de ejemplos como lo son:
* Registro de mediciones obtenidas de sensores (temperatura, humedad, presión, nivel de luz, voltaje, corriente, entre otros) integrados al dispositivo.
* Registro de eventos.

En resumen, un Data Logger consiste de alguna clase de sistema de adquisición, tal como sensores analogos, para recolectar datos. Tambien contienen alguna clase de memoria para almacenar cantidades considerables de datos durante un largos periodos de tiempo. 


**Registro local**: La información se puede registrar de diferentes maneras ([ejemplos](https://randomnerdtutorials.com/esp32-how-to-log-data/)), sin embargo vamos a realizar una leve clasificación:
* **Memoria interna**: En este caso se puede usar la flash del microcontrolador.
* **Uso de Memorias EEPROM**: Tambien se pueden usar chips EEPROM (memoria de solo lectura programable y borrable electrónicamente).
* **Tarjetas de memoria**: En este caso se emplean tarjetas de memoria como SD o microSD. Estas tarjetas proporcionan capacidad adicional de almacenamiento y facilitan la transferencia de datos a una computadora u otro dispositivo.

**Registro remoto**
En lugar de almacenar datos localmente, algunos data loggers pueden transmitir los datos recopilados a dispositivos como computadores, servidores o sistemas cloud. La transmisión puede ser alambrica (cable USB) o inalambrica mediante el uso de una conexión Wifi por ejemplo.

Los datos que se guardan pueden ser empleados para realizar un analisis posterior de estos.

### Algunos ejemplos...

Algunos proyectos en los cuales puede ser necesario el registro de datos:
1. Una estación climatica para el registro de la luz, la temperatura y la humedad sobre el tiempo.
2. Un GPS tracker and logger para mantener un registro de las hubicaciones en la que se han visitado a lo largo del dia.
3. El monitor de temperatura del computador de escritorio para reportar los datos sobre los componentes que se encuentran mas calientes.
4. Un light logger que mantiene un registro de cuando y por que tanto tiempo, las luces en la casa o la oficina estan encendidas.

<!--

### Para adaptar luego...
* https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial
  * SD cards come in two popular flavors - microSD and SD. The interface, code, structure, etc is all the same. The only differences is the size. MicroSD are much much smaller in physical size.
  * **Formatting notes**: 
    * Even though you can/could use your SD card 'raw' - it's most convenient to format the card to a filesystem. For the Arduino library we'll be discussing, and nearly every other SD library, the card must be formatted FAT16 or FAT32. Some only allow one or the other. The Arduino SD library can use either.
    * If you bought an SD card, chances are it's already pre-formatted with a FAT filesystem. However you may have problems with how the factory formats the card, or if it's an old card it needs to be reformatted. The Arduino SD library we use supports both FAT16 and FAT32 filesystems. 
  * Utilidad para formatear: https://www.sdcard.org/downloads/formatter/
  * Arduino Library & First Test (https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial/arduino-library)
  
https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images

* Required Materials
  * microSD Card w/ Minimum Card Size
  * microSD Card Reader
  * Linux Image
  * Single Board Computer (i.e. Raspberry Pi, NVIDIA Jetson Nano, etc.)
  * Internet Connection
* Memory card formater: https://www.sdcard.org/downloads/formatter/
* The Easy Way: To install your own image on your card we recommend software called [Etcher](https://etcher.balena.io/).

https://learn.sparkfun.com/tutorials/microsd-breakout-with-level-shifter-hookup-guide

https://learn.sparkfun.com/tutorials/microsd-shield-and-sd-breakout-hookup-guide


https://docs.arduino.cc/learn/programming/sd-guide/
* Probar el ejemplo

https://www.luisllamas.es/tarjeta-micro-sd-arduino/

https://naylampmechatronics.com/blog/38_tutorial-arduino-y-memoria-sd-y-micro-sd.html


## Hardware

### Componentes

La siguiente tabla muestra los componentes principales del circuito a montar:

|Componentes|Cantidad|Observaciones|
|---|---|---|
|ESP32|1||
|DHT11 Temperature and Humidity Module|1|Disponible en el kit Elegoo ([datasheet](https://cdn.sparkfun.com/assets/b/3/f/9/d/OKY3068-1.pdf))|

Es importante conocer los pines sensor. A continuación se muestra un mapa de estos ([link](https://components101.com/sensors/dht11-temperature-sensor)):

![conexion](DHT11–Temperature-Sensor-Pinout.jpg)

En kid Elegoo tiene un modulo que usa este sensor. Este se muestra a continuación junto con la descripción de los pines de conexión:

![dht11_elegoo](pines_elegoo.png)

### Esquematico

![esquematico](dh11-esp32_sch.png)

### Diagrama de conexión

La conexión entre el sensor DHT11 y el ESP32 se muestra en la siguiente tabla:

|ESP32|DHT11|
|---|---|
|P2 (GPIO2) |S|
|3.3V (VIN3.3V) |VSS|
|GND (GND) |GND|

A continuación se muestra el diagrama de conexión:

![esquematico](dh11-esp32_bb.jpg)

## Software

Este ejemplo se probo en arduino, se pide que repita el procedimiento usando Platformio.

### Configuración

#### Librerias empleadas

Se agregaron las siguientes librerias:

* **DHT**
  
  ![1](libreria_instalacion.png)

* **Adafruit Unified Sensor**

  ![2](libreria_unified_instalacion.png)

#### Programa

El programa codificado se muestra a continuación:

```ino


```

#### Test de la aplicación

Cuando se prueba la aplicación, la salida tiene la siguiente forma:

![3](esp32_dht11-serial.png)


## Otros recursos

La simulación del programa descargado se encuentra en ([link](https://wokwi.com/projects/357776308749643777))


-->
## Referencias

* https://randomnerdtutorials.com/esp32-how-to-log-data/
* https://randomnerdtutorials.com/esp32-data-logging-temperature-to-microsd-card/
* https://randomnerdtutorials.com/esp32-microsd-card-arduino/
* https://medium.com/@tara.haryono/esp32-data-visualization-and-data-logging-8dba973283b3
* https://www.instructables.com/Power-and-Temperature-Data-Logger-With-ESP32-and-A/
* https://www.hackster.io/anshul_apa/esp32-data-logger-with-dht22-google-sheets-using-chatgpt-9fb1bd
* https://github.com/G6EJD/ESP32_Data_Logging_Webserver
* https://esp32io.com/tutorials/esp32-sd-card
* https://www.instructables.com/ESP32-Micro-SD-Card-Interface/
* https://wokwi.com/projects/323656763409695316
* https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/sdmmc.html
* https://microcontrollerslab.com/microsd-card-esp32-arduino-ide/
* https://mischianti.org/how-to-use-sd-card-with-esp32-2/
* https://naylampmechatronics.com/blog/38_tutorial-arduino-y-memoria-sd-y-micro-sd.html
* https://www.arduino.cc/reference/en/libraries/sd/
* https://www.luisllamas.es/tarjeta-micro-sd-arduino/
* https://docs.arduino.cc/learn/programming/sd-guide/
* https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial
* https://learn.sparkfun.com/tutorials/microsd-shield-and-sd-breakout-hookup-guide/introduction
* https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images
* https://www.digikey.com/htmldatasheets/production/1848749/0/0/1/microsd-shield-and-sd-breakout-hookup-guide.html
* https://learn.sparkfun.com/tutorials/microsd-breakout-with-level-shifter-hookup-guide/all
* https://wiki.seeedstudio.com/SD_Card_shield_V4.0/
* https://wiki.seeedstudio.com/SD_Card_Shield_V3.0/
* https://wiki.seeedstudio.com/SD_Card_Shield/
* https://learn.adafruit.com/adafruit-data-logger-shield/using-the-sd-card
* https://maker.pro/arduino/tutorial/how-to-make-an-arduino-sd-card-data-logger-for-temperature-sensor-data
* https://docs.arduino.cc/tutorials/mkr-zero/mkr-zero-data-logger/
* https://hetpro-store.com/PDFs/micro-SD-y-Arduino.pdf
* https://esphome.io/
* https://lastminuteengineers.com/esp8266-dht11-dht22-web-server-tutorial/#google_vignette