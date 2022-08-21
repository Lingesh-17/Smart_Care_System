#! /usr/bin/python

# Imports
import RPi.GPIO as GPIO
import time
import requests

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)

# Turn off GPIO warnings
GPIO.setwarnings(False)

# Set a variable to hold the GPIO Pin identity
touch1=6
touch2=13
touch3=19
buzzer=11
led=9

GPIO.setup(touch1, GPIO.IN)
GPIO.setup(touch2, GPIO.IN)
GPIO.setup(touch3, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)


  
print("Smart_Care_Taker_System")

while True:
    time.sleep(0.4)
    if GPIO.input(touch1) ==1 :
        print("For_Food")
        r=requests.post('https://maker.ifttt.com/trigger/smart_care_taker_1/json/with/key/jq7kEoN_P1pQqYvf8WuMtnAaMnfxbez3YgV4fwW4k8C')
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(1)
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)
        
        
    elif GPIO.input(touch2) ==1 :
        print("For_Rest_Room")
        r=requests.post('https://maker.ifttt.com/trigger/smart_care_taker_4/json/with/key/jq7kEoN_P1pQqYvf8WuMtnAaMnfxbez3YgV4fwW4k8C')
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(1)
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)
        
    elif GPIO.input(touch3) ==1 :
        print("For_Medical_Help")
        r=requests.post('https://maker.ifttt.com/trigger/smart_care_taker_3/json/with/key/jq7kEoN_P1pQqYvf8WuMtnAaMnfxbez3YgV4fwW4k8C')
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(1)
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)
        
    else :
        print("NOTHING")


        
    
    