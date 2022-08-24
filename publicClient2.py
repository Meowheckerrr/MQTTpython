import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

#Connect to broker and create the client
mqttBroker ="mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_outside")
client.connect(mqttBroker)

while True:
    randNumber=uniform(30.0,31.0)
    client.publish("temperature",randNumber)
    print("Outside temerature " + str(randNumber) + "to topic: temperature")
    time.sleep(1)
