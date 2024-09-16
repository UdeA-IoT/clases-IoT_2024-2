from _thread import start_new_thread

from kivy.clock import mainthread
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen

from comm import Listener, Publisher


class IoT(Screen):
    estadoLuz = BooleanProperty(False)
    imagen_luz = StringProperty('light_off.png')

    def __init__(self, **kw):
        super().__init__(**kw)
        escuchador = Listener(self)
        try:
            start_new_thread(escuchador.start, ())
        except Exception as ex:
            print("Error: no se pudo iniciar el hilo. ex: {}".format(ex))


    def alternarLuz(self):
        if not(self.estadoLuz):
            Publisher.send_message('ON')
        else:
            Publisher.send_message('OFF')


    @mainthread
    def procesarMensajeLuz(self, msg):
        print(msg)
        self.estadoLuz = not self.estadoLuz
        if self.estadoLuz:
            self.imagen_luz = 'light_on.png'
        else:
            self.imagen_luz = 'light_off.png'