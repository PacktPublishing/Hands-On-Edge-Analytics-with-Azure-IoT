from loramessage import LoRaMessage
from time import sleep

message = LoRaMessage()

while True:
    message.send_message("heater_enabled: False")
    print("heater_enabled: False")
    sleep(2)
    message.send_message("heater_enabled: True")
    print("heater_enabled: True")
    sleep(2)
