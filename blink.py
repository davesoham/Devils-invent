#Test Blinking
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

num=12
while(num>0):
    
    GPIO.output(4,True)
    time.sleep(2)
    GPIO.output(4,False)
    time.sleep(2)
    num=num-1

print("The demo has ended")
    




