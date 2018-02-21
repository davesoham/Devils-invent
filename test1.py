from PIL import Image
import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setwarnings(False)

path = "/home/pi/Desktop/prototype"
dirs = os.listdir(path)
prev = 0
imageList=[]
for file1 in dirs:
    if file1.endswith(".jpg"):
        imageList.append(file1)

imageList.sort()
results=[]
for file1 in imageList:
    img = Image.open(str(file1))
    print (file1)
    pixels = img.getdata()
    count = 0
    total = 0
    for r,g,b in pixels:
        total += 1
        if g > b and g > r and b < 140 and r < 140:
            count += 1
    perc = round(count/total*100,2)
    results.append(perc)
##    print (str(perc)+"%")
    change = prev - perc
    if abs(change) == perc:
        change = 0
        changed=change
        results.append(changed)
    elif(change>=10.00):
        num=12
        while(num>0):
    
            GPIO.output(4,True)
            time.sleep(0.2)
            GPIO.output(4,False)
            time.sleep(0.2)
            num -= 1
##        GPIO.output(4,True)
    changed=round(change,2)
    results.append(changed)
##    print(changed)
    prev = perc
    num=0

    print("Green Color Density---> {}".format(results[0]))
    print("Percentage difference--> {}%".format(results[1]))
    print("")
    print("")
    print("*******NEXT THREE HOURS*****")

    results=[]
    

        
print("*****************************")
print(" ")
print("Information sent to database")
