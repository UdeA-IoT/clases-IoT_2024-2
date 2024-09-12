from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from typing import Annotated
import uvicorn 
import os

import serial
import serial.tools.list_ports

app = FastAPI()
app.led_status = False
app.port = None
app.serial = None

app.mount("/static", StaticFiles(directory="static"), 
          name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
def root():
    return {"App": "Ready"}

@app.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    if app.serial != None:
        # Verificacion del estado del serial 
        if app.serial.isOpen() == True:
            print("Puerto serial desconectado...")
            app.serial.close()
    # Lista de los puertos
    comlist = serial.tools.list_ports.comports()
    puertos = []
    for element in comlist:
      puertos.append(element.device)
    # Actualización de la template asociada a la conexión
    return templates.TemplateResponse("index.html", {"request": request, "puertos": puertos})

@app.get("/control")
async def control(request: Request, port: str):
    app.port = port
    serial_speed = 115200
    print(f"Iniciando conexión serial con el puerto {app.port} a {serial_speed} bps")
    app.serial = serial.Serial(app.port, serial_speed)
    if app.serial == None:
        return {"Connection": "Fail"}
    else:
        # return {"Connection": "Open"}
        return templates.TemplateResponse("control.html", {"request": request, "puerto": app.port})

@app.get("/led_change")
async def led_on(request: Request):
    # Cambio del estado del led al opuesto
    app.led_status = not(app.led_status)
    if app.led_status:
        # Envio del comando de encendido del led
        print("LED: On")
        app.serial.write(b'1')
    else:
        # Envio del comando de apagado del led
        print("LED: Off")
        app.serial.write(b'0')
    # Actualización de la template asociada al control del led
    return templates.TemplateResponse("control.html", {"request": request, "puerto": app.port})

@app.get("/disconnect")
async def disconnect(request: Request):
    app.serial.close()
    # Lista de puertos
    comlist = serial.tools.list_ports.comports()
    puertos = []
    for element in comlist:
      puertos.append(element.device)
    # Index
    return templates.TemplateResponse("index.html", {"request": request, "puertos": puertos})
    

if __name__ == "__main__":
    config = uvicorn.Config("server:app", log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()