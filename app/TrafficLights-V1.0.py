import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

south=[2,3,4]
west=[14,15,18]
north=[17,27,22]
east=[23,24,25]
red=[2,14,17,23]
yellow=[3,15,27,24]
green=[4,18,22,25]

all=south+west+north+east

def initialize():
    for led in all:
        GPIO.setup(led,GPIO.OUT)
        
def reset_all():
    for led in all:
        GPIO.output(led,GPIO.LOW)
    

def all_yellow():
    for led in yellow:
        GPIO.output(led,GPIO.HIGH)
        
def all_red():
    for led in red:
        GPIO.output(led,GPIO.HIGH)
    for led in yellow:
        GPIO.output(led,GPIO.LOW)
    for led in green:
        GPIO.output(led,GPIO.LOW)
        
def fun():
    for i in range(3):
        GPIO.output(south[i],GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(south[i],GPIO.LOW)
        GPIO.output(west[i],GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(west[i],GPIO.LOW)
        GPIO.output(north[i],GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(north[i],GPIO.LOW)
        GPIO.output(east[i],GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(east[i],GPIO.LOW)
      
initialize()
reset_all()

while True:
    fun()
    

   
        

   
   
    
    
    
    
    
    
    
    



