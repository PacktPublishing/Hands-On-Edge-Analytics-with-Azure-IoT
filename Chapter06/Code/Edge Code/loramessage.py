from network import LoRa
import socket

class LoRaMessage:
    def __init__(self):
        try:
            lora = LoRa(mode=LoRa.LORA,
                        frequency=915000000,
                        sf=12,
                        bandwidth=LoRa.BW_125KHZ,
                        coding_rate=LoRa.CODING_4_5)
        except:
            print("ERROR setting up LoRa!")

    def send_message(self, message):
        try:
            s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
            s.send(message)
        except:
            print("ERROR sending message!")
