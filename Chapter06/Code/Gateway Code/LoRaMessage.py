import config_lora
from machine import Pin, SPI
from sx127x import SX127x

class LoRaMessage:
    
    def get_message(self):
        device_pins = {
            'miso':19,
            'mosi':27,
            'ss':18,
            'sck':5,
            'dio_0':26,
            'reset':14 
        }

#         device_spi = SPI(baudrate = 10000000, 
#                 polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
#                 sck = Pin(device_pins['sck'], Pin.OUT, Pin.PULL_DOWN),
#                 mosi = Pin(device_pins['mosi'], Pin.OUT, Pin.PULL_UP),
#                 miso = Pin(device_pins['miso'], Pin.IN, Pin.PULL_UP))

        device_spi = SPI(baudrate = 10000000, 
                polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
                sck = Pin(device_pins['sck'], Pin.OUT, Pin.PULL_DOWN),
                mosi = Pin(device_pins['mosi'], Pin.OUT, Pin.PULL_UP),
                miso = Pin(device_pins['miso'], Pin.IN, Pin.PULL_UP))

        lora = SX127x(device_spi, pins=device_pins)
        print("Waiting for LoRa message.....")

        while True:
            if(lora.received_packet()):
                payload = lora.read_payload()
                status=str(payload)[18:-1]
                return (status)
                
