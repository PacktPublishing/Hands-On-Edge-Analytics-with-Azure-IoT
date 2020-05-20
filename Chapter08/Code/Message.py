import paho.mqtt.client as mqtt

class Message:
    
    def update(self, face_name):
        
        mqttc = mqtt.Client()
        mqttc.username_pw_set("miwdmkxc", "7SUxR3vX0v4N")
        mqttc.connect('hairdresser.cloudmqtt.com', 15912)
        mqttc.publish("face_name", face_name)
