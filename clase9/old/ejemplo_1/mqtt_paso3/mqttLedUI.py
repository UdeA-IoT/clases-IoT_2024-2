# -*- coding: utf-8 -*-

import sys
import glob
import paho.mqtt.client as mqtt

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.dropdown import DropDown
from kivy.logger import Logger

# Variables de la aplicacion
BROKER_IP = "127.0.0.1"
TOPIC = "room/light"
TOPIC_STATE = "room/light/state"

# Comandos
messLampOn = "on"
messLampOff = "off"

CLIENT_ID = "roomLamp_001"

class MainApp(App):   
        
    def on_start(self):      
        self.conect_status = False
        print("Configurando cliente mqtt...")
        self.mqtt_client=mqtt.Client(client_id=CLIENT_ID)
        self.mqtt_client.connect(BROKER_IP, 1883, 60) #connect to broker
        self.mqtt_client.on_connect = self.on_connect #attach function to callback
        self.mqtt_client.on_message = self.on_message #attach function to callback

        self.mqtt_client.loop_start() #start the loop        
        print("Subscribing to topic: ", TOPIC_STATE)
        self.mqtt_client.subscribe(TOPIC_STATE)
        return super().on_start()
        
    def on_stop(self):
        self.lightOFF()       
        self.mqtt_client.disconnect()        
        self.connection_status.text = "Desconectado"
        self.light_switch.disabled = True
        print("Conexion MQTT Terminada...")
        print("Cerrando la aplicacion")
            
    def build(self):        
        # -------------------------- Main layout -------------------------- #
        main_layout = BoxLayout(orientation="vertical")
        
        # -------------------------- Top layout -------------------------- #
        self.top_layout = BoxLayout(orientation="horizontal")        
        # Top layout - light_switch (Switch)
        self.light_switch = Switch(active=True)
        self.light_switch.disabled = True

        self.light_switch.bind(active=self.change_light)
        self.top_layout.add_widget(self.light_switch)        
        # Top layout - light_status (Label)
        self.light_status = Label(text='[b]LED[b]: OFF',markup=True)
        self.top_layout.add_widget(self.light_status)
        
        # -------------------------- Botton layout -------------------------- #
        self.botton_layout = BoxLayout(orientation="horizontal")                             
        # Botton layout - connection_status (Label)
        self.connection_status = Label(text='Desconectado')
        self.botton_layout.add_widget(self.connection_status)
                 
        # Agregando elementos al widget principal
        main_layout.add_widget(self.top_layout)
        main_layout.add_widget(self.botton_layout)        
        return main_layout
    
    def change_light(self, instance, value):
        if(value == True):            
            self.lightON()
        else:
            self.lightOFF()
    
    def on_connect(self, client, userdata, flags, rc):
        if(rc == 0):
            print("Conexión MQTT aceptada")
            self.conect_status = True
            self.connection_status.text = "Conectado"             
            self.light_switch.disabled = False
            self.conect_status = True
        else:
            print("Conexión MQTT rechazada")
            self.conect_status = False
        # ToDo: Agregar el caso donde no sea posible la conexion

    def on_message(self, mqttc, obj, msg):
        print(msg.payload)
        if(msg.payload == b'on'):
            self.light_status.text='[b]LED[b]: ON'
        else:
            self.light_status.text='[b]LED[b]: OFF'

    def lightON(self):
        print("--> Encendiendo la lampara\n")
        self.mqtt_client.publish(TOPIC, messLampOn)  # Uso de publish para prender la lampara

    def lightOFF(self):
        print("--> Apagando la lampara\n")
        self.mqtt_client.publish(TOPIC, messLampOff) # Uso de publish para apagar la lampara

if __name__ == "__main__":
    app = MainApp()
    app.run()