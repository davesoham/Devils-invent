from PIL import Image
import os

path = "/home/pi/Desktop/prototype"
dirs = os.listdir(path)
prev = 0
for file in dirs:
    if file.endswith(".jpg"):
        img = Image.open(str(file))
        print (file)
        pixels = img.getdata()
        count = 0
        total = 0
        for r,g,b in pixels:
            total += 1
            if g > b and g > r and b < 140 and r < 140:
                count += 1
        perc = round(count/total*100,2)
        print (str(perc)+"%")
    

        
print("*****************************")
print(" ")
print("Information sent to database")


