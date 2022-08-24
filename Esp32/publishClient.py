
#Mqtt main libary 


from umqtt.simple import MQTTClient

import time
import ubinascii
import machine
import micropython
import network
import esp
#from bme680 import *
#from machine import Pin, I2C


networkName = 'zsystem'
networkPassword = 'zang670623'

mqttBroker='122.117.14.208'
port=3390

clientID = ubinascii.hexlify(machine.unique_id())

#create topic 

publishMessagesTopic = b'meowhecker/messages'

#Hold the last message before you sent  
lastMessage = 0

#the time between each message setnt
messageInterval =1

#Connet the ESP to your local network

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(networkName, networkPassword)

while station.isconnected() == False:
  print("Wait to connect")
  time.sleep(2)
print('connect successful')


#connect to MQTT broker
def connectMqtt():  
  
  global clientID, mqttBroker
  
  #Establish client  
  client = MQTTClient(clientID, mqttBroker, port=port, user='test', password='test')
  client.connect()
  print(f'connect to {mqttBroker} MqttBroker')
  
  
  return client
  
#Restart and Reconnect
def reconnect():
  print('Reconnecting...')
  time.sleep(5)
  machine.reset()
  
try:
  client = connectMqtt()
  #print(1)
except OSError as e:
  print('false')
  #reconnect()


while True:
  
  client.publish(publishMessagesTopic,b'阿晟好帥')
  time.sleep(1)
  
  #print(1)




  
