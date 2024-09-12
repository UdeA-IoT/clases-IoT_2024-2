# Parte 2 - Creación del API para controlar el arduino

## Prerequisitos

Antes de iniciar debera tener instaladas las libreias FastAPI y Uvicorn. Para mas información puede ir al siguiente [link](https://fastapi.tiangolo.com/tutorial/):

```bash
python -m pip install fastapi uvicorn[standard]
```

Tambien, es necesario que se lleve a cabo la instalación de pydantyc

```bash
pip install pydantic
```

En RealPython hay un excelente tutorial conocido que muestra como construir Web APIs usando FastAPI (**Using FastAPI to Build Python Web APIs** - [link](https://realpython.com/fastapi-python-web-apis/))

## Software

### API Endpoints

Los endpoints se muestran a continuación:

|HTTP method | API endpoint |Descrición|
|---|---|---|
|```GET``` | ```/``` |	Muestra el estado de la aplicación |
|```GET``` | ```/ports``` |	Obtiene una lista de puertos |
|```GET``` | ```/connect/<port_id>``` |	Conecta la aplicación al puerto serial elegido |
|```GET``` | ```/disconnect``` | Desconecta la aplicación del puerto serial |
|```GET``` | ```/on``` | Enciende el led (Una vez la aplicación se ha conectado) |
|```GET``` | ```/off``` | Apaga el led (Una vez la aplicación se ha desconectado) |

El script de python en el que se realiza la implementación usando FastAPI se muestra a continuación :

```python
# Serial
import serial
import serial.tools.list_ports

# Pydantic
from pydantic import Field

# FastAPI
from fastapi import FastAPI

SERIAL_SPEED = 115200

app = FastAPI()
app.serial = None

@app.get("/")
async def home():
    return {"App": "Ready"}

@app.get("/ports")
async def listPorts():
   comlist = serial.tools.list_ports.comports()
   ports = []
   for element in comlist:
      ports.append(element.device)
   return {"ports": ports}

@app.get("/connect/{port_id}")
async def connect(port_id): 
    print("Iniciando conexión...")
    app.serial = serial.Serial(port_id, SERIAL_SPEED)
    if app.serial == None:
        return {"Connection": "Fail"}
    else:
        return {"Connection": "Open Port" + str(app.serial.port) + " at " + str(app.serial.baudrate)}

@app.get("/disconnect") 
async def disconnect():
    app.serial.close()
    return {"Connection": "Close"}

@app.get("/on")
async def led_on():
    app.serial.write(b'1')
    return {"led":"on"}

@app.get("/off")
async def led_off():
    print(app.serial)
    app.serial.write(b'0')
    return {"led":"off"}
```

## Probando la aplicación

Asumiento que la aplicación se guardo como **api_serialLed_esp32.py**, para ejecutar la aplicación se emplea el comando:

```bash
uvicorn api_serialLed_esp32:app --reload
```

Si todo esta bien, deberia salir algo en consola similar a:

![api_consola](terminal_output.png)

Por otro lado, si se ejecuta en el navegador la URL **127.0.0.1:8000** la salida sera:

![api_browser](browser_output.png)

Para el resto de las pruebas basta con poner en la URL del navegados cualquiera de los endpoints mensionados en la tabla al principio, o para mayor comodidad pasarlo a traves de la interfaz web facilitada por FastAPI para llevar a cabo las pruebas. Para acceder a esta se coloca en el campo de la URL del navegador **127.0.0.1:8000/docs** lo cual deberia arrojar una salida como la que se muestra a continuación:

![api_browser_docs](serial_web1.png)

### Pruebas

La siguiente tabla resume los comandos **curl** empleados para hacer las pruebas:

|Comando |Descrición|
|---|---|
|```curl  URL``` | Estado de ejecución de la aplicación en el servidor|
|```curl URL/ports``` |	Lista los puertos seriales disponibles |
|```curl URL/connect/<port_id>``` | Conecta la aplicación al puerto serial elegido |
|```curl URL/on``` | Enciende el led (Una vez la aplicación se ha conectado) |
|```curl URL/off``` | Apaga el led (Una vez la aplicación se ha desconectado) |
|```curl URL/disconnect``` |  Apaga el led (Una vez la aplicación se ha desconectado) |

Al ejecutar los comandos anteriores en la aplicación, el resultado fue similar al siguiente:

![curl_cmd](curl_test.png)

El resultado se usar las herramientas de FastAPI para las pruebas se muestra a continuación:

1. **Estado de la aplicación**: Si la aplicación inicia sin problemas el resultado sera como el mostrado en la siguiente figura:
   
   ![app_state](serial_web2.png)

2. **Lista de puertos disponibles**: A continuación se muestran los puertos disponibles:
   
   ![ports](serial_web3.png)

3. **Conexión al puerto serial**: La conexión se hace teniendo en cuenta la lista de puertos disponibles. A continuación se muestra el caso cuando el puerto disponible es el **COM18**:
   
   ![conect_serial](serial_web3.png)

   Adicionalmente, se muestra un ejemplo de realizar esta petición usando el Postman:

   ![postman_conect_serial](postman_test.png)

4. **Encendido del led**: Al enviar la petición para encender la luz, si todo esta bien, se debe encender el led en la ESP32:

   ![led_on](serial_web4.png)
  

5. **Apagado del led**: El resultado de apagar el led se muestra en la siguiente figura:
   
   ![led_off](serial_web5.png)

6. **Desconexión del puerto serial**: Finalmente, para liberar el puerto serial, se emplea la petición para desconectar tal y como se muestra en la siguiente figura:

   ![disconnect_serial](serial_web6.png)


## Referencias

1. https://fastapi.tiangolo.com/
2. https://fastapi.tiangolo.com/tutorial/
3. https://fastapi.tiangolo.com/es/tutorial/
4. https://realpython.com/api-integration-in-python/
5. https://realpython.com/flask-connexion-rest-api/
6. https://realpython.com/flask-connexion-rest-api-part-2/
7. https://realpython.com/flask-connexion-rest-api-part-3/
8. https://realpython.com/courses/python-rest-apis-with-fastapi/
