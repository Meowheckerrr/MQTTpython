
#Mqtt main libary 
from umqtt.simple import MQTTClient

import time
import ubinascii
import machine
import micropython
import network

import esp
esp.osdebug(None)

import gc
gc.collect()


#Network account password 
ssid = 'zsystem'
password = 'zang670623'


#mqtt server 
mqtt_server = '122.117.14.208'
port = 3390

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'meowhecker/message'


#mqtt:account/password 
user = 'test'
mqttpassword = 'test'


last_message = 0
message_interval = 5 #time between each message sent
counter = 0


#Connect the ESP to the network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')


print(station.ifconfig())



# print Chinese
def printChinese(msg):
  print(str(msg.decode('utf-8')))

def sub_cb(topic, msg):
  print((topic, msg))
  printChinese(msg)

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server,port=port,user=user,password=mqttpassword)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client



def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

while True:
    
  try:
    client = connect_and_subscrib 
    print(1)
  except OSError as e:
    restart_and_reconnect()


while True:
    
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      msg = b'Hello #%d' % counter
#       client.publish(topic_pub, "zzzz")
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()

