#define LED_BUILTIN 2 // opens serial port, sets data rate to 9600 bps

int incomingByte = 0; // for incoming serial data

#define ON '1'
#define OFF '0'

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    if(incomingByte == ON) {
      digitalWrite(LED_BUILTIN, LOW);      
    }
    else {
      digitalWrite(LED_BUILTIN, OFF);   
    }
  }
}
