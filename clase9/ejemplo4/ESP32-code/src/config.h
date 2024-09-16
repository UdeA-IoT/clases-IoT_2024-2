#pragma once
#include <string>

using namespace std;

// ESP32 I/O config
#define LIGHT_PIN 5

// WiFi credentials
const char *SSID = "IoT";
const char *PASSWORD = "1245678h";

// MQTT settings
const string ID = "thing-001";

const string BROKER = "192.168.43.55"; // "test.mosquito.org";
const string CLIENT_NAME = ID + "lamp_client";

const string TOPIC1 = "light_outbound";
const string TOPIC2 = "light_inbound";