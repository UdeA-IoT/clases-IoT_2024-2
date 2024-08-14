#include <Arduino.h>

// Puertos
#define LED 3

// Inicializacion
void setup() {
  pinMode(LED, OUTPUT);
}

// Ciclo infinito
void loop() {
  digitalWrite(LED, HIGH);   
  delay(1000);                       
  digitalWrite(LED, LOW);    
  delay(1000);                      
}