#include <Arduino.h>
#include <ArduinoJson.h>
#include "DHT.h"


#define SAMPLE_TIME 500
 
// --------------------------------- Entradas --------------------------------- //

// DTH11: Sensor de temperatura y humedad
#define DHTPIN 4     // Digital pin connected to the DHT sensor

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

DHT dht(DHTPIN, DHTTYPE);

// Potenciometro: Variable Analoga
#define ANALOG_PIN 15


// ------------------ Variables ------------------
bool sample_DHT11 = false;
int sample_th = 0;

// Allocate the JSON document
JsonDocument doc;

void setup() {
  Serial.begin(9600);
  Serial.println(F("System Ready..."));
  dht.begin();
}


void loop() {
  // Wait a few seconds between measurements.
  delay(SAMPLE_TIME);
  int sensorValue = analogRead(ANALOG_PIN);
  float sensorVoltage = (3.3*sensorValue)/4095; // ADC de 12 bits
  doc["sensor"] = "POT";
  // Add an array.
  doc["data"] = sensorVoltage;
  serializeJson(doc, Serial);
  Serial.println();
  sample_th++;



  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float H = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float T = dht.readTemperature();


  // Check if any reads failed and exit early (to try again).
  if (isnan(H) || isnan(T)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  if(sample_th%4 == 0) {
    // Captura de la temperatura (Cada 2 segundos)
    // Add values in the document
    doc["sensor"] = "DTH11";
    // Add an array.
    JsonArray data = doc["data"].to<JsonArray>();
    data.add(H);
    data.add(T);
    // Generate the minified JSON and send it to the Serial port.
    serializeJson(doc, Serial);
    // The above line prints:
    // {"sensor":"DTH11","time":1351824120,"data":[H,T]}

    // Start a new line
    Serial.println();
    sample_th = 0;
  }
}

