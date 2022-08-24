
import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network

import esp
esp.osdebug(None)
import gc
gc.collect()

networkName = 'zsystem'
networkPassword = 'zang670623'


mqttBroker='122.117.14.208'
port=3390


clientID = ubinascii.hexlify(machine.unique_id())

publishMessagesTopic  = b'meowhecker/public/messages'
subscribeMessageTopic = b'meowhecker/subscribe/messages'

lastMessage = 0
messageInterval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(networkName, networkPassword)

while station.isconnected() == False:
  print("Disconnect")
  time.sleep(1)
print('connect successfully')
print(station.ifconfig()) #show network information 





#main()
#CallbackFunction
def subscribeCallback(topic, msg):
  print((topic, msg))

    
    
#Connecte broker as well as to subscribe to a topic
def brokerConnectSubscribe():
  global clientID, mqttBroker, subscribeMessageTopic
  
  client = MQTTClient(clientID, mqttBroker, port=port, user='test', password='test')
  client.set_callback(subscribeCallback)
  
  #client connect to broker 
  client.connect()
  
  #subscribe to topic
  client.subscribe(subscribeMessageTopic)
  
  print(f'connect to Broker {mqttBroker} , Subscribe to {subscribeMessageTopic}')
  return client 
 
#Restart and Reconnect

def restartAndReconnect():
  print('Reconnecting...')
  time.sleep(5)
  machine.reset()

#Handler


try:
  client = brokerConnectSubscribe()
  #print(1)
except OSError as e:
  print("false")
  #restartAndReconnect()




while True:
  #print(1)
#send messages to subscribes 

#while True:
#  try:
#    client.check_msg()
#    if(time.time() - lastMessage) > messageInterval:
#      messages=f'sendMessage, messageConter {counter}'
#      client.publich(publishMessagesTopic, messages)
#      lastMessage = time.time()
#      counter ++
#  except OSError as e:
#    restartAndReconnect()
#

  
