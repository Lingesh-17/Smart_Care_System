from machine import Pin #for control I/O Devices
import time #for time delay
import urequests #for http get and post request
import network #for network operations


ssid=""  #your ssid
password=""  #you password

touch1=Pin(16, Pin.IN) #connect on ESP8266'S D0
touch2=Pin(5, Pin.IN)  #connect on ESP8266'S D1
touch3=Pin(4,Pin.IN)   #connect on ESP8266'S D2
touch4=Pin(2, Pin.IN)  #connect on ESP8266'S D4
buzzer=Pin(14, Pin.OUT)#connect on ESP8266'S D5
led=Pin(12, Pin.OUT)   #connect on ESP8266'S D6

wlan = network.WLAN(network.STA_IF) 
wlan.active(True)       
wlan.scan()
wlan.connect(ssid, password)
led.off()


if not wlan.isconnected():
    buzzer.off()
    time.sleep(0.1)
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
    time.sleep(0.1)
    wlan.connect(ssid, password)

else wlan.isconnected():
    print("WIFI CONNECTED")
    
    
while True:
    time.sleep(0.5)
    
    #touch sensor (1) for help
    if touch1.value()==1:
        buzzer.off()
        time.sleep(0.1)
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(0.1)
        urequest.get("https://maker.ifttt.com/trigger/help/json/with/key/esHgC3Njvhf0DP_sPr7PWVc28oVtmznpJQgjIqgO0Bw")
     
    #touch sensor (2) for food
    elif touch2.value()==1:
        buzzer.off()
        time.sleep(0.1)
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(0.1)
        urequest.get("https://maker.ifttt.com/trigger/food/json/with/key/esHgC3Njvhf0DP_sPr7PWVc28oVtmznpJQgjIqgO0Bw")
        
    #touch sensor (3) for rest_room
    elif touch3.value()==1:
        buzzer.off()
        time.sleep(0.1)
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(0.1)
        urequest.get("https://maker.ifttt.com/trigger/rest_room/json/with/key/esHgC3Njvhf0DP_sPr7PWVc28oVtmznpJQgjIqgO0Bw")
        
    #touch sensor (4) hospital's choice
    elif touch4.value()==1:
        buzzer.off()
        time.sleep(0.1)
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(0.1)
        #urequest.get("Hospital's Choice")        
    
    
    else:
        print("NO INPUT ARRIVED")