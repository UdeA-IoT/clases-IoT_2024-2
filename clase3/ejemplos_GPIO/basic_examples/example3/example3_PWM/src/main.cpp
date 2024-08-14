#include <Arduino.h>

#define YD_ESP32

// Puertos
#if defined(YD_ESP32)
const int ledPin = 3;    // GPIO3
#else
const int ledPin = 2;    // GPIO2
#endif


// Inicializacion
void setup() {
  // nothing happens in setup
}

// Ciclo infinito
void loop() {
  for (int fadeValue = 0 ; fadeValue <= 255; fadeValue += 5) {
    analogWrite(ledPin, fadeValue);
    delay(30);
  }

  for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
    analogWrite(ledPin, fadeValue);
    delay(30);
  }
}