import kivy
kivy.require('1.10.1')

import serial

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

sensor = serial.Serial()
sensor.baudrate = 9600
sensor.port = 'COM3'
sensor.timeout = 1
sensor.open()

class MainWindow(GridLayout):

    lblReading: Label

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.cols = 1

        self.add_widget(Label(text='Serial Reading:'))

        self.lblReading = Label(text='xx')
        self.add_widget(self.lblReading)

        Clock.schedule_once(self.update_reading, 1)

    def update_reading(self, dt):
        reading = int(sensor.readline())
        # print('reading: ', reading)
        self.lblReading.text = str(reading)

        Clock.schedule_once(self.update_reading, 1)


class MyApp(App):

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
