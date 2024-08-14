# Ejemplo 2 - Implementación del sensor de ultrasonido en el ESP32

## Descripción

En el siguiente ejemplo muestra, usando el monitor serial, la distancia en centimetros y pulgadas el cual se implemento en el ejemplo 1 ([link](../arduino/README.md)) para el arduino UNO.

Este ejemplo fue adaptado de  **SparkFun Inventor's Kit Experiment Guide - Project 3: Motion** ([link](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/project-3-motion)) para el ESP32.

## Hardware

La siguiente tabla muestra los componentes principales del circuito a montar:


| Item # | Cantidad | Descripción    | Información |
| ------ | -------- | -------------- | ----------- |
| 1      | 1        | ESP32          | N/A         |
| 2      | 1        | Sensor de ultrasonido HC-SR04  | HC-SR04 Ultrasonic Sensor Module User Guide ([link](https://www.handsontec.com/dataspecs/HC-SR04-Ultrasonic.pdf)) |
| 3      | 1        | RGB LED  | Elegoo - 37 in 1 Sensor Modules Kit ([link](https://www.elegoo.com/products/elegoo-37-in-1-sensor-kit)) |

### Esquematico

<p align="center">
  <img src="esp32_ultrasonido2_sch.png">
</p>

### Conexión entre los componentes

La conexión entre el sensor de ultrasonido se muestra en la siguiente tabla:


|ESP32|HC-SR04|
|---|---|
|5V|VCC|
|GPIO5|Trig|
|GPIO18|Echo|
|GND|GND|


|ESP32|RGB LED (KY-009)|
|---|---|
|GPIO4|R|
|GPIO2|G|
|GPIO2|B|
|GND|GND|


A continuación se muestra la conexión entre los componentes:

<p align="center">
  <img src="esp32_ultrasonido2_bb.png">
</p>

## Software

### Código

A continuación se muestra el programa que se ejecuta en el ESP32, el cual basicamente es el mismo programa implementado para el Arduino UNO pero empleando otros pines:

```ino
/**
   Hardware Connections:

      ESP32 | HC-SR04
    -------------------
      5V    |   VCC
      5     |   Trig
      18    |   Echo
      GND   |   GND

      ESP32 | HC-SR04
    -------------------
      4    |   R
      0    |   G
      2    |   B
      GND  |   GND
*/

// Pins

// Sensor de ultrasonido
const int trigPin = 5;
const int echoPin = 18;

// Led RGB
const int redPin = 4;             //pin to control the red LED inside the RGB LED
const int greenPin = 0;           //pin to control the green LED inside the RGB LED
const int bluePin = 2;            //pin to control the blue LED inside the RGB LED

float distance = 0;               //stores the distance measured by the distance sensor

void setup() {
  Serial.begin (9600);        //set up a serial connection with the computer

  pinMode(trigPin, OUTPUT);   //the trigger pin will output pulses of electricity
  pinMode(echoPin, INPUT);    //the echo pin will measure the duration of pulses coming back from the distance sensor

  //set the RGB LED pins to output
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  distance = getDistance();   //variable to store the distance measured by the sensor

  Serial.print(distance);     //print the distance that was measured
  Serial.println(" in");      //print units after the distance

  if (distance <= 10) {                       //if the object is close

    //make the RGB LED red
    analogWrite(redPin, 255);
    analogWrite(greenPin, 0);
    analogWrite(bluePin, 0);

  } else if (10 < distance && distance < 20) { //if the object is a medium distance

    //make the RGB LED yellow
    analogWrite(redPin, 255);
    analogWrite(greenPin, 50);
    analogWrite(bluePin, 0);

  } else {                                    //if the object is far away

    //make the RGB LED green
    analogWrite(redPin, 0);
    analogWrite(greenPin, 255);
    analogWrite(bluePin, 0);
  }

  delay(50);      //delay 50ms between each reading
}

//------------------ FUNCTIONS -------------------------------

//RETURNS THE DISTANCE MEASURED BY THE HC-SR04 DISTANCE SENSOR
float getDistance() {
  float echoTime;                   //variable to store the time it takes for a ping to bounce off an object
  float calculatedDistance;         //variable to store the distance calculated from the echo time

  //send out an ultrasonic pulse that's 10ms long
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  echoTime = pulseIn(echoPin, HIGH);      //use the pulsein command to see how long it takes for the
                                          //pulse to bounce back to the sensor

  calculatedDistance = echoTime / 148.0;  //calculate the distance of the object that reflected the pulse (half the bounce time multiplied by the speed of sound)

  return calculatedDistance;              //send back the distance that was calculated
}
```

## Pruebas y simulación

### Arduino IDE - Test

La siguiente figura muestra la salida en el monitor serial cuando el programa es ejecutado:

<!--

<p align="center">
  <img src="ultrasonido_esp32_serial.png">
</p>
-->

### Wokwi - Simulación

Para comprender el funcionamiento del programa, puede seguir el siguiente [link](https://wokwi.com/projects/391350736522728449) cuyo montaje se muestra a continuación:

<p align="center">
  <img src="esp32-ultrasonido_sim2.png">
</p>

## Referencias
1. https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-3b-distance-sensor
2. https://github.com/sparkfun/HC-SR04_UltrasonicSensor
3. https://www.sparkfun.com/products/15569
4. https://www.handsontec.com/dataspecs/HC-SR04-Ultrasonic.pdf
5. https://randomnerdtutorials.com/esp32-hc-sr04-ultrasonic-arduino/
6. https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/
7. https://randomnerdtutorials.com/esp8266-nodemcu-hc-sr04-ultrasonic-arduino/
8. https://spot.pcc.edu/~dgoldman/#engr101
9. https://www.festi.info/boxes.py/
10. https://gritlab.org/
11. https://gritlab.org/project-design-guide/