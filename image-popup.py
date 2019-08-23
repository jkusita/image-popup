# image-popup.py - opens an image in a folder and keeps it open for a period of time the closes it then opens up a new one.

# TODO: write code that pops up the image randomly or in order?


from PIL import Image
import os, time
import psutil


image_folder = "/Users/ramteechua/Desktop/image-popup-folder/"
os.chdir(image_folder)

while True:
    for file in os.listdir():
        
        # 30 mins = 1800 seconds
        # TODO: maybe make this into minutes using mathematical operations?
        seconds = 3 
        # This is needed in case DSfile shows up in folder
        try:
            image = Image.open(file)
            # Displays image
            image.show()
        except OSError:
            pass
        
        # Display the time left.1,800
        while seconds != 0:
            print(seconds)  
            seconds -= 1
            time.sleep(1)

        # Hides image
        for proc in psutil.process_iter():
        # Personal comment: you can put print(proc) here to see all the proc running? and so you can see the name there you can put it in if proc.name() == "":
            if proc.name() == "Preview":
                proc.kill()
            
        print(os.listdir()) # for testing
        # TODO: make a try for OSError, put comments on it describing for dstore etc

# TODO: experiment by putting the image in the folder and see if the program updates it.