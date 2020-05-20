from umqtt.robust import MQTTClient

class HeaterStatus:
    
    def update(self, status):
        
        client = MQTTClient(client_id="router",
                    server="hairdresser.cloudmqtt.com",
                    user="miwdmkxc",
                    password="7SUxR3vX0v4N",
                    port=15912)

        client.connect()
        client.publish("heater_enabled",status)
