/* ----- Include Libraries ----- */
#include <WiFi.h>
#include <PubSubClient.h>

/* ----- Third Libraries ----- */
#include "config.h"  // Set your network SSID and password in this file
#include "MQTT.hpp"
#include "ESP32_Utils.hpp"
#include "ESP32_Utils_MQTT.hpp"

//Libraries for the temperature sensor
#include <OneWire.h> // by Paul Stoffregen
#include <DallasTemperature.h> // by Miles Burton

/* ----- Ports ----- */
#define RELAY LED_BUILTIN    // Pin for builtin led in the esp32 board (Simulate a relay)
const int oneWireBus = 4;    // Pin to connect the temp sensor, pin 4 in my case.


/* ----- Variables ----- */
int light_state = 0;         // Initial led's state
int counter_KA = 0;          //Counter for sending keep alive message each 5 seconds

char msg[50];

/* Topics */
char topic[] = "home";



/* ----- Helper functions (Third party libraries) ----- */

//Set the onewire interface
OneWire oneWire(oneWireBus);

//Set the temp sensor to use the onewire interface
DallasTemperature sensors(&oneWire);

/* ----- Main funtions ----- */

// setup
void setup() {
  // Ports inicialization
  pinMode(RELAY, OUTPUT);    // BUILTIN_LED pin as an output
  digitalWrite(RELAY, LOW);  // Light initial state is OFF
  // Serial setup
  Serial.begin(115200);  
  ConnectWiFi_STA(false);
  InitMqtt();
  delay(1000);
}

// loop
void loop() {
  // Read the temperature value
  Serial.print("Sending a command to sensors");
  sensors.requestTemperatures();

  // Temperature read in celcius
  float temperatureC = sensors.getTempCByIndex(0);

  // Write data to serial monitor 
  Serial.print("Temperature sensor : ");
  Serial.print(temperatureC);
  Serial.println("°C");

  HandleMqtt();

  // Send temperature value to the MQTT server
  // Device ID for temperature : 2
  snprintf (msg, 50, "2,%.2f", temperatureC);
  Serial.print("Publish message: ");
  Serial.println(msg);
  PublisMqttString(topic, msg);

  //Process for sending Keep Alive messages
  counter_KA++;
  if(counter_KA == 10){
    counter_KA = 0;
    /* Since this ESP32 implemented two devices Light(id = 0) and
    *  temperature (id = 2), this node must send two KA messages
    */
    // DeviceID=0,ONLINE_STATE
    snprintf (msg, 50, "0,100" );
    Serial.print("Sending Light keep alive message to Rpi: ");
    Serial.println(msg);
    PublisMqttString(topic, msg);
    // DeviceID,ONLINE_STATE
    snprintf (msg, 50, "2,100" );
    Serial.print("Sending Temp keep alive message to Rpi: ");
    Serial.println(msg);
    PublisMqttString(topic, msg);
  }
  // Read temperature each 5 seconds
  delay(500);
}