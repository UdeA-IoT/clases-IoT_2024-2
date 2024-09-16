


## Aplicación ESP32

**Archivo de configuración**: platformio.ini

```ini
[env:nodemcu-32s]
platform = espressif32
board = nodemcu-32s
framework = arduino
lib_deps = 
    knolleary/PubSubClient @ 2.8
    bblanchon/ArduinoJson @ 6.17.3
```

**Archivo cabecera**: config.h

```h
#include <string>

using namespace std;

// WiFi credentials
const char *SSID = "SSID";
const char *PASSWORD = "PASSWORD";

// MQTT settings
const string ID_SERVER = "SERVER_IOT_UDEA";
const string ID_THING = "IOT_UDEA-001";

const string BROKER = "IP_BROKER";
const string CLIENT_NAME = ID_THING + "sensor_client";

const string CLIENT_TELEMETRY_TOPIC = ID_SERVER + "/telemetry";
const string SERVER_COMMAND_TOPIC = ID_THING + "/commands";
```

**Archivo principal**: main.cpp

```cpp
#include <Arduino.h>
#include <WiFi.h>
#include <ArduinoJson.h>
#include <PubSubClient.h>

#include "config.h"

#define LIGHT_PIN LED_BUILTIN // Pin to control the light with P2 (GPIO2)
#define ANALOG_SENSOR 34      // Pin to measure the analog variable P15 (GPIO15)

WiFiClient espClient;
PubSubClient client(espClient); // Setup MQTT client

void connectWiFi() {
  delay(500);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.println("Connecting to WiFi...");
    WiFi.begin(SSID, PASSWORD);
    delay(500);
  }
  Serial.println("Connected!");
}

// Handle incomming messages from the broker
void clientCallback(char *topic, uint8_t *payload, unsigned int length) {
  char buff[length + 1];
  for (int i = 0; i < length; i++) {
    buff[i] = (char)payload[i];
  }
  buff[length] = '\0';

  Serial.print("Message received:");
  Serial.println(buff);

  DynamicJsonDocument doc(1024);
  deserializeJson(doc, buff);
  JsonObject obj = doc.as<JsonObject>();

  bool alarm_on = obj["alarm_on"];

  if (alarm_on) {
    digitalWrite(LIGHT_PIN, HIGH);
  }
  else {
    digitalWrite(LIGHT_PIN, LOW);
  }
}

void reconnectMQTTClient() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect(CLIENT_NAME.c_str())) {
      Serial.println("connected");
      client.subscribe(SERVER_COMMAND_TOPIC.c_str());
    }
    else {
      Serial.print("Retying in 5 seconds - failed, rc=");
      Serial.println(client.state());
      delay(5000);
    }
  }
}

void createMQTTClient() {
  client.setServer(BROKER.c_str(), 1883);
  client.setCallback(clientCallback);
  reconnectMQTTClient();
}

void setup() {
  Serial.begin(9600);
  while (!Serial)
    ; // Wait for Serial to be ready
  delay(1000);

  pinMode(ANALOG_SENSOR, INPUT);
  pinMode(LIGHT_PIN, OUTPUT);

  connectWiFi();
  createMQTTClient();
}

void loop() {
  reconnectMQTTClient();
  client.loop();

  int analog_variable = analogRead(ANALOG_SENSOR);

  DynamicJsonDocument doc(1024);
  doc["analog_variable"] = analog_variable;

  string telemetry;
  serializeJson(doc, telemetry);

  Serial.print("Sending telemetry ");
  Serial.println(telemetry.c_str());

  client.publish(CLIENT_TELEMETRY_TOPIC.c_str(), telemetry.c_str());

  delay(1000);
}
```


## Aplicación del cliente paho (Servidor)

```python
import json
import time

import paho.mqtt.client as mqtt

UMBRAL = 2500

id_server = 'SERVER_IOT_UDEA'
id_thing = 'IOT_UDEA-001'

client_telemetry_topic = id_server + '/telemetry'
server_command_topic = id_thing + '/commands'
client_name = id_server + 'sensor_client'

mqtt_client = mqtt.Client(client_name)
#mqtt_client.connect('test.mosquitto.org')
mqtt_client.connect('127.0.0.1')

mqtt_client.loop_start()

def send_alarm_command(client, state):
    command = { 'alarm_on' : state }
    print("Sending message:", command)
    client.publish(server_command_topic, json.dumps(command))

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    if payload['analog_variable'] > UMBRAL:
        send_alarm_command(client, True)
    else:
        send_alarm_command(client, False)


mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)
```