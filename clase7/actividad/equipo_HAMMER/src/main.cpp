#include <Arduino.h>
#include <WiFi.h>
#include <WiFiClient.h>


// Definir PINES
#define PIN_X 34   //  P2 (GPIO02 - ADC11)
#define PIN_Y 35   //  P4 (GPIO04 - ADC12)
#define PIN_SW 15 //  P15 (GPIO15)

// Conexión WiFi
#define SSID "GerarC"
#define PASSWORD "Baracunatana"

// Dweet.io
#define HOST "dweet.io"
#define HTTP_PORT 80
#define THING "joystick27"

// Funciones necesarias
void wifi_connection();
WiFiClient dweet_connection();
void send_request(WiFiClient client, int x, int y, int z);

// Información de los pines
int valueX = 0;        //  Analog
int valueY = 0;        //  Analog
int valueZ = 0;        //  Digital


void setup() {
  Serial.begin(9600);
  wifi_connection();  
}

void loop() {
  delay(100);
  valueX = analogRead(PIN_X); 
  valueY = analogRead(PIN_Y); 
  valueZ = digitalRead(PIN_SW);

  Serial.print("X:");
  Serial.print(valueX, DEC); 
  Serial.print(" | Y:"); 
  Serial.print(valueY, DEC); 
  Serial.print(" | Z: "); 
  Serial.println(valueZ, DEC); 


  WiFiClient client = dweet_connection();
  send_request(client, valueX, valueY, valueZ);
}


void wifi_connection(){
  /*
  Serial.print("Connecting to ");
  Serial.println(SSID);
  */
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  /*
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  */
}

WiFiClient dweet_connection(){
  Serial.print("Connecting to ");
  Serial.println(HOST);

  // Use WiFiClient class to create TCP connections
  WiFiClient client;
  if (!client.connect(HOST, HTTP_PORT)) {
    Serial.println("connection failed");
    return NULL;
  } else return client;
}

void send_request(WiFiClient client, int x, int y, int z){
  // We now create a URI for the request
  String url = "http://dweet.io/dweet/for/" + String(THING) + "?x_axis=" + String(x) + "&y_axis=" + String(y) + "&z_axis=" + String(z);

  // Send request
  Serial.print("Requesting URL: ");
  Serial.println(url);
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + HOST + "\r\n" +
               "Connection: close\r\n\r\n");

  unsigned long timeout = millis();
  while (client.available() == 0) {
    if (millis() - timeout > 1000) {
      Serial.println(">>> Client Timeout !");
      client.stop();
      return;
    }
  }
}