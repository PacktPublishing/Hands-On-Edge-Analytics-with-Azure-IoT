from azure.iot.device import IoTHubDeviceClient, Message
from time import sleep

CONNECTION_STRING = "[PASTE IN CONNECTION STRING]"

temp = "25"
humidity = "50"
message_text = "{'temperature':'" + temp + "', 'humidity':'" + humidity + "'}"


def connect_client():
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        return client
    except KeyboardInterrupt:
        print("Stopped!")


def run_simulation(client):
    client = client
    while True:
        message = Message(message_text)
        print("Sending message: {}".format(message))
        client.send_message(message)
        print("Message successfully sent")
        sleep(10)


if __name__ == '__main__':
    print("Started simulated device")
    print("Press Ctrl-C to exit")
    run_simulation(connect_client())
