#include <Arduino.h>

// ----- Pines ------
//const int voltsInPin = 4;
#define voltsInPin 4
//const int ledPin = 2;
#define ledPin 2

void setup() {
  pinMode(ledPin, OUTPUT);
}
void loop() {
  int rawReading = analogRead(voltsInPin);
  int period = map(rawReading, 0, 4095, 100, 500);
  digitalWrite(ledPin, HIGH);
  delay(period);
  digitalWrite(ledPin, LOW);
  delay(period);
}
