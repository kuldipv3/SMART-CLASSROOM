from Adafruit_IO import MQTTClient
import random
import sys
import RPi.GPIO as gp
import readCount

gp.setwarnings(False)
gp.setmode(gp.BOARD)
led1=29
led2=32
led3=33
led4=36
gp.setup(led1,gp.OUT)
gp.setup(led2,gp.OUT)
gp.setup(led3,gp.OUT)
gp.setup(led4,gp.OUT)

status = ""
username = "kuldipv3"
adaIdKey = "2ac876601c1f40f1b40c522a3e5806bc"


def connected(client):
    print("connected to adafruit")
    client.subscribe("Master Switch")


def disconnected(client):
    print("disconnected from adafruit")
    sys.exit()


def message(client,feed_id,payload):
    print("{0} is {1} ",feed_id,payload)
    if(feed_id =="Master Switch"):
        if(payload =="ON"):
            global status
            status = "MS"
            print(status)
            gp.output(led1,1)
            gp.output(led2,1)
            gp.output(led3,1)
            gp.output(led4,1)
    if(feed_id =="Master Switch"):
        if(payload =="OFF"):
            global status
            status = "xx"
            print(status)
            gp.output(led1,0)
            gp.output(led2,0)
            gp.output(led3,0)
            gp.output(led4,0)

client = MQTTClient(username,adaIdKey)
client.on_connect=connected
client.on_disconnected=disconnected
client.on_message=message
client.connect()
client.loop_background()
while True:
    
    if status == "MS":
        pass
    else:
        count = readCount.checkCount()
        print(count)
        if count == "0":
            gp.output(led1,0)
            gp.output(led2,0)
            gp.output(led3,0)
            gp.output(led4,0)
        if count == "1":
            gp.output(led1,1)
            gp.output(led2,0)
            gp.output(led3,0)
            gp.output(led4,0)
        if count == "2":
            gp.output(led1,1)
            gp.output(led2,1)
            gp.output(led3,0)
            gp.output(led4,0)
        if count == "3":
            gp.output(led1,1)
            gp.output(led2,1)
            gp.output(led3,1)
            gp.output(led4,0)
        if count == "4":
            gp.output(led1,1)
            gp.output(led2,1)
            gp.output(led3,1)
            gp.output(led4,1)
