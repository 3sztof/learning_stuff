﻿import paho.mqtt.client as mqtt

# Define event callbacks
def on_connect(mosq, obj, rc,):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log


# Connect
mqttc.username_pw_set("erjbgdfp:erjbgdfp", "Q4EzmE4smYBZvLIx3yp4-QEEJg46QvKB")
mqttc.connect("golden-kangaroo.rmq.cloudamqp.com", 1883)

# Start subscribe, with QoS level 0
mqttc.subscribe("hello/world", 0)

mqttc.loop_forever()
# Publish a message
mqttc.publish("test", "my message")


## Continue the network loop, exit when an error occurs
#rc = 0
#while rc == 0:
#    rc = mqttc.loop()
#print("rc: " + str(rc))