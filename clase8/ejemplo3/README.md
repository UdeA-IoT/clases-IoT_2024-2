# Ejemplo 3 - Creación del API para controlar el encendido y apagado de un led conectado al Arduino

Continuación del ejemplo [link](../../P3/RS_232/ejemplo4/README.md) 

**Ver**: 
* https://github.com/UdeA-IoT/clases-IoT_capa-percepcion_2023-2/tree/main/dia4/serial-esp32-platformio
* https://github.com/UdeA-IoT/clases-IoT_capa-percepcion_2023-2/tree/main/dia4/uso_platformio
* https://github.com/UdeA-IoT/clases-IoT_capa-percepcion_2023-2/tree/main/dia4/serial-esp32-platformio/paso6

# Elementos necesarios

Entorno local

```bash
python -m venv env
.\cv_env\Scripts\activate 
```

```
pip install fastapi
pip install "uvicorn[standard]"
pip install pyserial
pip install python-multipart
```

```bash
pip freeze > requirements.txt
```


```bash
python -m venv cv_env
.\cv_env\Scripts\activate 
pip install -r requirements.txt
```

# Asumiendo que ya todo esta instalado

# Programa ESP32

[link](https://wokwi.com/projects/393263531512991745)

```cpp
#include <Arduino.h>

// I/O pines
#define LED_PIN 18

// Commands
#define ON '1'
#define OFF '0'

int incomingByte = 0; // for incoming serial data

/** setup **/
void setup() {  
  pinMode(LED_PIN, OUTPUT); // initialize digital pin LED_BUILTIN as an output.
  digitalWrite(LED_PIN, LOW);
  Serial.begin(115200);         // opens serial port, sets data rate to 115200 bps
  // Serial.write("Puerto serial inicializado...\n");
  
}

/** loop **/
void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    if(incomingByte == ON) {
      digitalWrite(LED_PIN, HIGH);    
      // Serial.write("Led encendido\n");     
    }
    else {
      digitalWrite(LED_PIN, LOW);   
      // Serial.write("Led Apagado\n");
    }
  }
}
```

## Referencias

1. https://www.delftstack.com/
2. https://www.delftstack.com/howto/python/list-serial-ports-in-python/