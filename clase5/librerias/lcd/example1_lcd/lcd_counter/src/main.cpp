#include <Arduino.h>
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 22, en = 23, d4 = 4, d5 = 0, d6 = 2, d7 = 15;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int counter = 0;

void setup() {
  Serial.begin(9600);
  Serial.println(F("LCD test!"));

  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("LCD Ready!");
  lcd.setCursor(0, 1);
  delay(2000);  
  lcd.print("Counter: ");
}

void loop() {
  Serial.print("Counter: ");   
  Serial.println(counter);    
  lcd.print(counter,DEC);
  delay(1000);
  counter++;
  lcd.setCursor(9, 1);
}
