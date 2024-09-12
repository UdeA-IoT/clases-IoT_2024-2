# Ejemplo 1

En el siguiente ejemplo se muestra como realizar una petición web empleando:
1. El comando curl.
2. Usando el Postman.
3. Usando el Arduino.

## Usando el Curl

Un punto de partida para trabajar esta herramienta se resume en la siguiente resumen hecho por [Julia Evans](https://twitter.com/b0rk):

![Curl](https://wizardzines.com/comics/curl/curl.png)

Si se desea profundizar mas, en la web hay abundante material, de manera que lo animamos. En nuestro caso a modo de Test vamos a ejecutar el siguiente comando:

```bash
curl -v tmb.gr/hello.json
```

El resultado de ejecutar este comando desde una consola de linux se muestra en la siguiente imagen:

![curl](curl.png)

Online, tambien encuentra esta herramienta en [Run Curl Commands Online](https://reqbin.com/curl). Lo animamos a que haga el ensayo y observe el resultado al ejecutar el mismo comando previamente ejecutado.

## Usando el Postman

El [Postman](https://www.postman.com/) es una aplicación que permite la realización de pruebas API. Este cliente HTTP nos da la posibilidad de testear 'HTTP requests' a través de una interfaz gráfica de usuario de manera amigable. Es ampliamente usado y segun el siguiente [enlace](https://rapidapi.com/blog/best-api-testing-tools/) es de las mejores herramientas para realizar testing API. A continuación se muestra el resultado de hacer la prueba anterior usando postman:

![test-postman](test-postman.png)

## Usando el Arduino

El siguiente ejemplo fue tomado del siguiente [link](https://github.com/tamberg/fhnw-iot/blob/master/03/Arduino/ESP8266_WiFiClient/ESP8266_WiFiClient.ino)

* **Codigo**: [ejemplo1.ino](ejemplo1.ino). (**Nota**: No olvidar modificar el ejemplo de acuerdo a los parametros de su red local).

```arduino
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
```

El resultado de ejecutar el código anterior en el arduino se muestra en:

![salida-serial](salida-serial.png)

## Conclusión

Como se puede ver de los ejemplos anteriormente realizados, es posible usar el arduino como un cliente web lo cual permite que este pueda comunicarse con cualquier plataforma IoT empleando cualquier API definida. En el suguiente ejemplo vamos a explorar un caso de uso.