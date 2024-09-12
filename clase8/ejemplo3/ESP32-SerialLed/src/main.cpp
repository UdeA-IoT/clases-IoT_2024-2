#include <Arduino.h>

// I/O pines
#define LED_PIN 18

// Commands
#define ON '1'
#define OFF '0'

int incomingByte = 0; // for incoming serial data

/** setup **/
void setup() {  
  pinMode(LED_PIN, OUTPUT); // initialize digital pin LED_BUILTIN as an output.
  digitalWrite(LED_PIN, LOW);
  Serial.begin(115200);         // opens serial port, sets data rate to 115200 bps
  // Serial.write("Puerto serial inicializado...\n");
  
}

/** loop **/
void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    if(incomingByte == ON) {
      digitalWrite(LED_PIN, HIGH);    
      // Serial.write("Led encendido\n");     
    }
    else {
      digitalWrite(LED_PIN, LOW);   
      // Serial.write("Led Apagado\n");
    }
  }
}