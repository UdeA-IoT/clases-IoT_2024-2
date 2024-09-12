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