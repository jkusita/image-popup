# image-popup.py - opens an image in a folder and keeps it open for a period of time the closes it then opens up a new one.

# TODO: write code that pops up the image randomly or in order?


from PIL import Image
import os, time
import psutil


image_folder = "/Users/ramteechua/Desktop/image-popup-folder/"
os.chdir(image_folder)

while True:
    for file in os.listdir():
        seconds = 5
        image = Image.open(file)
        # Displays image
        image.show()

        # Display the time left.
        while seconds != 0:
            print(seconds)  
            seconds -= 1
            time.sleep(1)

        # Hides image
        for proc in psutil.process_iter():
        # Personal comment: you can put print(proc) here to see all the proc running? and so you can see the name there you can put it in if proc.name() == "":
            if proc.name() == "Preview":
                proc.kill()
            
    