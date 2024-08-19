#include <Arduino.h>

// #define NODE_ESP32
#define YD_ESP32

#if defined(NODE_ESP32)
  #define LED 2   //  (GPIO2)
#elif defined(YD_ESP32)
  #define LED 3   //  (GPIO3)
#else
  #define LED 5   
#endif


// Puertos
const int buttonPin = 4;           //  (GPIO4)
const int ledPin =  LED;           //  Depende de la placa usada

// variables will change
int buttonState = 0;         

// Inicializacion
void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

// Ciclo infinito
void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}

