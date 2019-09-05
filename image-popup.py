# image-popup.py - opens an image in a folder and keeps it open for a period of time the closes it then opens up a new one.

# TODO: write code that pops up the image randomly or in order?


from PIL import Image
import os, time, random
import psutil


image_folder = "/Users/ramteechua/Desktop/image-popup-folder/"
os.chdir(image_folder)

minutes_input = int(input("How many minutes?: "))

while True:
    minutes = minutes_input
    
    # Randomy selects a file from the folder.
    file = random.choice(os.listdir())

    # This is needed in case DSfile shows up in folder
    try:    
        image = Image.open(file)
        # Displays image
        image.show()
    except OSError:
        pass
    
    # Display the time left.
    while minutes != 0:
        print(minutes)  
        time.sleep(60)
        minutes -= 1

    # Closes image
    for proc in psutil.process_iter():
    # Personal comment: you can put print(proc) here to see all the proc running? and so you can see the name there you can put it in if proc.name() == "name_here":
        if proc.name() == "Preview":
            proc.kill()
        

