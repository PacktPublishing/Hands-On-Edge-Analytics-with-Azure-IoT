import pycom

class Heater:

    def __init__(self):
        pycom.heartbeat(False)

    def on(self):
        pycom.rgbled(0xFF0000)  # Red

    def off(self):
        pycom.rgbled(0x000000)  # Black
