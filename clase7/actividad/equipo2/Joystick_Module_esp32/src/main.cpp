#include <Arduino.h>

/**
   Hardware Connections:

    | ESP32	| DTH11 |
    |---|---|
    |GND   |   GND (pin 1 - izquierda) |
    |3.3   |   +5 (pin 2) |
    |P2    |   VRx (pin 3) |
    |P4    |   VRy (pin 4) |
    |P15   |   SW (pin 5 - derecha) |
*/

const int pinX = 2;    //  P2 (GPIO02 - ADC11)
const int pinY = 4;    //  P4 (GPIO04 - ADC12)
const int pinSW = 15;  //  P15 (GPIO15)
int valueX = 0;        //  Analog
int valueY = 0;        //  Analog
int valueZ = 0;        //  Digital

void setup() {
  Serial.begin(9600);
}

void loop() {
  valueX = analogRead(pinX); 
  Serial.print("X:");
  Serial.print(valueX, DEC); 
  valueY = analogRead(pinY); 
  Serial.print(" | Y:"); 
  Serial.print(valueY, DEC); 
  valueZ = digitalRead(pinSW);
  Serial.print(" | Z: "); 
  Serial.println(valueZ, DEC); 
  delay(100);
}