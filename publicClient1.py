import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

#Connect to broker and create the client
mqttBroker ="mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_inside")
client.connect(mqttBroker)

while True:
    randNumber=uniform(25.0,26.0)
    client.publish("temperature",randNumber)
    print(" Outside temerature " + str(randNumber) + "to topic: temperature")
    time.sleep(1)
