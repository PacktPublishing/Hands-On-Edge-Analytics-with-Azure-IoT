from LoRaMessage import LoRaMessage
from HeaterStatus import HeaterStatus

message=LoRaMessage()
heater_status=HeaterStatus()

while True:
    status=message.get_message()
    heater_status.update(status)
    

