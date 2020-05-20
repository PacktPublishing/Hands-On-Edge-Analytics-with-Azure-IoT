from dht11 import DHT11
from heater import Heater
from loramessage import LoRaMessage
from time import sleep

dht11 = DHT11()
message = LoRaMessage()
heater = Heater()
temp_threshold = 25
max_cycles = 2
num_cycles = 0
a=100

#while True:
while a>0:
    message.send_message("heater_enabled: True")
    print("heater_enabled: True")
    #temperature = dht11.get_temperature()
    temperature = dht11.get_sim_temperature(temp_threshold)
    if(temperature < temp_threshold):
        num_cycles += 1
        heater.on()
    else:
        heater.off()

    if(num_cycles >= max_cycles):
        heater.off()
        num_cycles = 0
        message.send_message("heater_enabled: False")
        print("heater_enabled: False")
        sleep(5)
    a=a-1
    print(a)
    sleep(2)
