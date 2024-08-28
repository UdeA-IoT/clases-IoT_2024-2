# Protocolos de comunicación entre los componentes de un nodo

## Objetivos

> * Comprender los diferentes protocolos de comunicación empleados por los componentes básicos de un nodo.
> * Explorar algunos ejemplos de aplicación

## Referencias principales

1. Lección 3 **Interact with the phisycal world** ([link](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/2-deeper-dive/README.md)) del curso **IoT for Beginners** ([link](https://github.com/microsoft/IoT-For-Beginners)) de Microsoft.

## Conceptos abordados

1. Comunicación serial [[link]](https://udea-iot.github.io/UdeA_IoT-page/docs/sesiones/percepcion/sesion4/)
2. Comunicación usando One Wire (En construcción...)
3. Comunicación usando I2C (En construcción...)
4. Comunicación usando SPI (En construcción...)


## Protocolos IoT comumente usados

Para permitir la comunicación entre dispositivos de usan diferentes tipos de protocolos los cuales se pueden clasificar en dos grandes grupos:

|Tipo|Caracteristicas|Ejemplos|
|---|---|---|
|Inalambricos|Facilitan la movilidad entre los dispositivos conectados; sin embargo, tienen limitantes en lo que respecta el consumo de potencia, el rango de cobertura y (comparativamente) las tasas de transferencia y throughput.|802.11 WiFi, Bluetooth, Low Power Wide Area Network (LPWAN), LoRa, SigFox|
|Alambricos|Superan algunas de las limitaciones de la tecnología inalámbrica, en particular las velocidades de datos y la eficiencia energética; sin embargo, puede requerir la instalación de una infraestructura significativa por lo que solo se adaptan bien a dispositivos estacionarios.|SPI, I2C, Ethernet, RS232|

## Comunicación entre sensores

Actualmente disponemos de diferentes IC de memoria, sensores digitales, dispositivos de protección, fuentes de alimentación programables, potenciómetros digitales, IC de radiofrecuencia, etc. Todos necesitan comunicarse entre sí o con microcontroladores, microprocesadores, FPGA o ASIC. El propósito de estas comunicaciones entre dispositivos puede variar mucho. Puede ser que la programación extraiga información, proporcionando una señal para iniciar la ejecución de una acción.

En la actualidad, se disponen de una gran cantidad de circuitos integrados IC como: memorias, sensores digitales, potenciometros digitales y circuitos de radio frecuencia entre otros. Todos estos dispositivos realizan diferentes operaciones que dependen de la información que es enviada hacia y desde otros componentes digitales similares. 

Para permitir la comuniación de estos dispositivos entre si y con otros como los microcontrolaores se emplean difenrentes protocolos de comunicación los cuales se han definido por medio de estandares comunes con el fin de posibilitar la comunicación entre dispositivos sin depender del fabricante.

En esta parte se mostrará, de manera resumida, algunos de los diferentes tipos de protocolos de comunicación serial haciendo enfasis en los que se listan a continuación:
* RS-232 [[link]](RS_232/README.md)
* One Wire. [[link]](one-wire/README.md)
* I2C [[link]](I2C/README.md)
* SPI [[link]](SPI/README.md)

## Referencias

* https://learn.sparkfun.com/tutorials/serial-communication/all
* https://resources.altium.com/es/p/spi-versus-i2c-how-choose-best-protocol-your-memory-chips
* https://resources.altium.com/es/p/i2c-vs-spi-vs-uart-how-layout-these-common-buses
* https://www.analog.com/en/resources/analog-dialogue/articles/uart-a-hardware-communication-protocol.html
* https://resources.altium.com/p/serial-communications-protocols-introduction
* https://resources.altium.com/p/serial-communications-protocols-part-two-uart
* https://resources.altium.com/p/serial-communications-protocols-part-three-rs-232
* https://resources.altium.com/p/serial-communications-protocols-rs-485
* https://resources.altium.com/p/serial-communications-protocols-part-5-spi
* https://resources.altium.com/p/6-serial-communications-protocols-i2c
* https://resources.altium.com/p/7-serial-communications-protocols-1-wire
* https://resources.altium.com/p/serial-communications-protocols-can-and-lin
* https://resources.altium.com/es/p/spi-versus-i2c-how-choose-best-protocol-your-memory-chips
* https://hackmd.io/2oRlH_ogSWigu6HOc99TYw
* https://learn.sparkfun.com/tutorials/installing-an-arduino-library/all
* https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use/arduino-libraries
* https://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries
* https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries
* https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-installing-a-library
* https://github.com/UdeA-IoT/actividad-4
* https://www.arduino.cc/reference/en/libraries/
* https://esp32io.com/tutorials/esp32-keypad
* https://deepbluembedded.com/esp32-keypad-lcd-example-arduino/
* https://docs.simplefoc.com/library_platformio
* https://randomnerdtutorials.com/vs-code-platformio-ide-esp32-esp8266-arduino/
* https://dronebotworkshop.com/platformio/
