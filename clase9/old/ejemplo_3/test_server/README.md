# Test server

Informacion del test del server...


Requisitos:
* Paho
* Json

```python
import json
import time

import paho.mqtt.client as mqtt

UMBRAL = 2500

id = '<ID>'

client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'
client_name = id + 'sensor_client'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

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

