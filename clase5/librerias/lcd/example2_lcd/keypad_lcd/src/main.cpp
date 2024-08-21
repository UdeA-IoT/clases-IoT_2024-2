#include <Arduino.h>
#include <Keypad.h>
#include <LiquidCrystal.h>

// ---------------- Variables ---------------- //
// Clave
String password = "1234";
String input = "";
int num_key;
int key_len = 4;
// Estado
bool clave_completa = false;  // Indica que se metieron key_len digitos
bool ok = false;              // Indica si la clave ingresada fue correcta

// ---------------- Entradas ---------------- //
// ---- Keypad ----
const byte ROWS = 4; // Four rows
const byte COLS = 4; // Three columns
    
// Define the Keymap
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'#','0','*','D'}
};
    
// Conections ESP32 - Keypad
#define ROW1 13
#define ROW2 12
#define ROW3 14
#define ROW4 27
#define COL1 26
#define COL2 25
#define COL3 33
#define COL4 32 
// Connect keypad ROW1, ROW2, ROW3 and ROW4 to these Arduino pins.
byte rowPins[ROWS] = { ROW1, ROW2, ROW3, ROW4 };
// Connect keypad COL0, COL1, COL2 and COL3 to these Arduino pins.
byte colPins[COLS] = { COL1, COL2, COL3, COL4 }; 
    
// Create the Keypad
Keypad kpd = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

// ---------------- Salidas ---------------- //
// Led
const int ledpin = 17;  
// buzzer
const int buzzerPin = 5;   
int buzzerState = LOW;        // the current state of the output pin
int freq = 2000;
int channel = 0;
int resolution = 8;
// LCD
#define LCD_ROWS 2
#define LCD_COLUMNS 16
const int rs = 22, en = 23, d4 = 4, d5 = 0, d6 = 2, d7 = 15;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // Inicializacion
  num_key = 0; // Numero de teclas ingresadas
  // Inicializacion del pin
  pinMode(ledpin,OUTPUT);
  digitalWrite(ledpin, LOW);
  // Init pwm (buzzer)
  ledcSetup(channel, freq, resolution);
  ledcAttachPin(buzzerPin, channel);
  // Init LCD
  lcd.begin(LCD_COLUMNS, LCD_ROWS);
  lcd.print("Clave: ");
  lcd.setCursor(0, 1);
  lcd.print("Puerta: ");
  lcd.print("cerrada");
  // Init serial
  Serial.begin(9600);
  Serial.println("System Ok...");
  lcd.setCursor(7, 0);
  lcd.blink();
}
    
void loop() {  
  char key = kpd.getKey();
  // Procesamiento de la tecla ingresada
  if(key) { 
    input.concat(key);    
    // Check for a valid key    
    Serial.println(key); // Impresion de la tecla en el monitor serial
    lcd.print("*"); // * en el LCD
    num_key++;
    if(num_key == key_len) {
      // Se metieron num_key digitos
      Serial.println(input);
      if (input.equals(password)) {
        // Clave correcta
        Serial.println("OK");    
        ok = true; 
      }
      else {
        // Clave errada
        Serial.println("Fail");    
        ok = false;     
      }
      input = "";
      num_key = 0; 
      clave_completa = true;    
    }     
    // Generacion del beep
    ledcWriteTone(channel, 1500);
    delay(100);
    ledcWriteTone(channel, 0);
  }
  // Verificacion de que la clave se metio completa
  if(clave_completa == true) {
    if(ok == true) {
      // Clave correcta (apertura puerta)
      lcd.noBlink();
      lcd.setCursor(8, 1);
      // Mensaje de apertura en el LCD
      lcd.print("abierta");
      digitalWrite(ledpin, HIGH); // Indicador puerta abierta  
      delay(3000);  // Tiempo que la puerta esta abierta
      digitalWrite(ledpin, LOW); // Indicador puerta cerrada
      // Mensaje de puerta cerrada en el LCD
      lcd.setCursor(8, 1);
      lcd.print("cerrada");
      // Borrado de los asteriscos
      lcd.setCursor(7, 0);
      lcd.print("    ");
      lcd.setCursor(7, 0); 
      lcd.blink();
      ok = false; // Se pasa nuevamente al estado inicial
    }
    else {
      delay(1000); // Espera de 1 seg
      // Borrado de los asteriscos
      lcd.setCursor(7, 0);
      lcd.print("    ");
      lcd.setCursor(7, 0); 
    }
    clave_completa = false;
  }
}