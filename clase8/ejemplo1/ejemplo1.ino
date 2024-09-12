#include <WiFi.h>
/*
Codigo adaptado de: https://github.com/tamberg/fhnw-iot/blob/master/03/Arduino/ESP8266_WiFiClient/ESP8266_WiFiClient.ino
*/

//////////////////////
// WiFi Definitions //
//////////////////////

// WiFi network
const char* ssid     = "SSID";
const char* password = "SSID_PASS";

void setup() {
  setupWiFi();
  serverRequest();
}

void loop() {
  
}

void setupWiFi() {
  // Connecting to a WiFi network
  Serial.begin(115200);
  Serial.println();
  Serial.println();
  Serial.println("Connecting to WiFi network: " + String(ssid));
  WiFi.begin(ssid, pwd);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void serverRequest() {
  const char *host = "tmb.gr";
  const char *path = "/hello.json";
  const int port = 80;

  // connect to remote host
  WiFiClient client;
  if (client.connect(host, port)) {   
    /*
    Command in PC: curl -v tmb.gr/hello.json
    */

    // send HTTP request
    client.print("GET ");
    client.print(path);
    client.print(" HTTP/1.1\r\n");
    client.print("Host: ");
    client.print(host);
    client.print("\r\n");
    client.print("Connection: close\r\n\r\n");

    // read HTTP response
    while (client.connected() || client.available()) {
      int ch = client.read();
      while (ch >= 0) {
          Serial.print((char) ch);
          ch = client.read();
      }
    }
  }
}