import pycom
from machine import Pin
from dth import DTH
import uos

class DHT11:
    temp_sensor = DTH(Pin('P4', mode=Pin.OPEN_DRAIN),0)

    def get_temperature(self):
        return self.temp_sensor.read().temperature

    def get_humidity(self):
        return self.temp_sensor.read().humidity

    def get_sim_temperature(self, temp_threshold):
        random_num = uos.urandom(1)[0]
        if(random_num > 100):
            return temp_threshold-1
        else:
            return temp_threshold + 1
