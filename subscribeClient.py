from email import message
import paho.mqtt.client as mqtt
import time

#Connect to broker and create the client
mqttBroker ="mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)


def callBackMessage(client, userdata, message):
    print("Received message:" , str(message.payload.decode("utf-8")))

client.loop_start()

client.subscribe('temperature')
client.on_message = callBackMessage

time.sleep(30)
client.loop_end()