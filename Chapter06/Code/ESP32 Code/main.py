import esp32
import time
from machine import Pin

led = Pin(5, Pin.OUT)

while True:
    hall_sensor = esp32.hall_sensor()
    #print(hall_sensor)
    #print("Temperature:")
    #print(esp32.raw_temperature())
    if(hall_sensor > 100):
        led.value(False)
    else:
        led.value(True)
    #led.value(not led.value())
    time.sleep(1)
    
    