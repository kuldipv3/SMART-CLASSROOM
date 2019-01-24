import json
import requests
import time

countn = 0

url = "https://dweet.io/get/latest/dweet/for/kv3sc"

def checkCount():
    response = requests.get(url)
    data = json.loads(response.text)
    details = data["with"][0]
    countn = details["content"]["count"]
    
    if(countn == 0):
        return "0"
    if(countn>0 and countn<3):
        return "1"
    if(countn>2 and countn<5):
        return "2"
    if(countn>4 and countn<7):
        return "3"
    if(countn>6 and countn<9):
        return "4"
    
