import paho.mqtt.client as mqttc
from paho.mqtt import publish

OUTBOUND_TOPIC = "light_outbound"
INBOUND_TOPIC = "light_inbound"
BROKER_URL = "localhost"
BROKER_PORT = 1883

class Publisher:

    @staticmethod
    def send_message(message):
        try:
            publish.single(OUTBOUND_TOPIC, message,
                           hostname= BROKER_URL, port = BROKER_PORT)
        except Exception as ex:
            print("Error enviando un mensaje ex: {}".format(ex))

class Listener:

    def __init__(self, observador):
        self.client = mqttc.Client(mqttc.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.observador = observador
        try:
            self.client.connect(BROKER_URL, BROKER_PORT, 60)
        except:
            print("sin conexión al broker")

    def start(self):
        print('looping')
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc, properties):
        print("Conectado ", str(rc), INBOUND_TOPIC)
        client.subscribe(INBOUND_TOPIC)


    def on_message(self, client, userdata, msg):
        print("Mensaje recibido: {}".format(msg))
        self.observador.procesarMensajeLuz(msg.payload.decode("utf-8"))