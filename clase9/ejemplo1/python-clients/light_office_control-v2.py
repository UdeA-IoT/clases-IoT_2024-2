import paho.mqtt.client as mqtt
import time

# Variables de la aplicacion
BROKER_IP = "test.mosquitto.org"
TOPIC = "home/office/lamp"

# Comandos
messLampOn = "ON"
messLampOff = "OFF"

# Mensajes
messReceibed = False

def on_connect(mqttc, obj, flags, rc, properties):
    if rc == 0:
        print("Conexion MQTT Establecida")
    else:
        print("No se pudo establecer la conexion (return code %d)\n", rc)
    

# 1. Creacion de la isntanca del cliente
CLIENT_ID = "officeLamp"
mqtt_client = mqtt.Client(callback_api_version =  mqtt.CallbackAPIVersion.VERSION2,
                          client_id=CLIENT_ID)
mqtt_client.on_connect = on_connect

# 2. Incovacion del metodo connect
mqtt_client.connect(BROKER_IP, 1883, 60)

# 3. Llamando el loop para mantener el flujo de trafico de red en el broker
# 4. No se llevo a cabo en este caso.
mqtt_client.loop_start()
time.sleep(2) # Para esperar que la conexion se establezca antes de desplegar el menu

print("SISTEMA DE CONTROL DE LA LAMPARA DE LA SALA")
while True:
    print("Menu de control de la sala")
    print("1. Encender lampara")
    print("2. Apagar lampara")
    print("3. Salir de la aplicacion")
    opc = input("Seleccione una opcion: ")
    if opc == '1':
        print("--> Encendiendo la lampara\n")
        mqtt_client.publish(TOPIC,messLampOn)  # Uso de publish para prender la lampara
    elif opc == '2':
        print("--> Apagando la lampara\n")
        mqtt_client.publish(TOPIC,messLampOff) # Uso de publish para apagar la lampara
    elif opc == '3':
        messReceibed = False
        print("--> Chao bambino\n")
        break
    else:
        messReceibed = False
        print("--> OPCION INVALIDA\n")
mqtt_client.loop_stop()
