from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from iot import IoT


class Contenedor(App):
    sm = ScreenManager()

    def build(self):
        self.sm.add_widget(IoT(name='iot'))
        return self.sm



Contenedor().run()
