from tkinter import *
from tkinter import messagebox
from time import strftime
from PIL import Image, ImageTk
from pynput import keyboard
import webbrowser
import PIL
import random
import subprocess
import errno
import keyboard
import os
import sys

#Adding random stuff for functionality, ask if you need
root = Tk()
root.geometry("420x420")
root.resizable(0,0)
root.title('Cypclock 0.2')
#Above code is rules relating to the shape, title, and other properties of the window it's self

#open the background image
image = Image.open("images/gfs.jpg")

#make sure it's the right size (it already is but lets make sure for learning reasons)
image = image.resize((420, 420), Image.LANCZOS)

#convert the image to a PhotoImage object
photo_image = ImageTk.PhotoImage(image)

# Create a Label widget and add the PhotoImage to it
background_label = Label(root, image=photo_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Adding Variables, can be numbers or strings
new = 1
url = "https://www.youtube.com/watch?v=Q44DA9-TH2o&list=PLLGIaswzK8nerfBww5vX312Bt2B5A24om"
wikirandomurl = "https://en.wikipedia.org/wiki/Special:Random"


#Adding commands, or something idk, to be called later. I don't fully understand how they work yet, but I know enough to write this.
def openwebrandomdeclassified():
   urls = ['https://www.butts.com', 'https://boob.com', 'https://ass.com']
   random_url = random.choice(urls)
   webbrowser.open(random_url)
def openweb():
   webbrowser.open(url,new=new)
def expand ():
   pass
def openwebrandomwiki():
   webbrowser.open(wikirandomurl,new=new)


   #Bug here, if you close this newly created window and then press the button to relaunch, it fails. Idk why. 
def openwindow():
    import time
    time.sleep(1)
    import gui
def fortnite():
   messagebox.showerror("Error", "No added functionality :(")  #Bug Fixed

# Create the drop-down menu
menu = Menu(root)

# Create the "File" menu with a command for the "Open" option
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="Open", command=fortnite)

# Add the "File" menu to the menu bar
menu.add_cascade(label="File", menu=file_menu)

# Create a second (launch) menu with a command for the "Save" option
launch_menu = Menu(menu, tearoff=0)
launch_menu.add_command(label="Korn AMVS", command=openweb)

# Add the launch menu to the menu bar
menu.add_cascade(label="Launch", menu=launch_menu)

# Add the menu bar to the main window
root.config(menu=menu)

#Create the "Random" menu with a command for 3 blank inputs to be filled later.
random_menu = Menu(menu, tearoff=0)
random_menu.add_command(label="Random URLs", command=openwebrandomdeclassified)
random_menu.add_command(label="Random Wikipedia", command=openwebrandomwiki)

#Add the "Random" menu to the menu bar
menu.add_cascade(label="Random", menu=random_menu)


# button code, commented out because it's made redundant after adding the top menus. 
# Will remove later, is only staying so 666 can read the code and understand what was happening before.


#random_url_button = Button(root,
#                  text="Random URLs",
 #                 command=openwebrandomdeclassified,
  #                font=("calibri", 24),
   #               fg="blue")
#random_url_button.pack(pady=100)

korn_amv_button = Button(root,
                  text="Mem Editor",
                  command=openwindow,
                  font=("calibri", 24),
                  fg="blue")
korn_amv_button.pack(pady=100)



# clock code
Label(root,
      text = 'KillGod420',
      background = 'pink',
      foreground = 'blue',
      font = 'arial 20 bold').pack(side=BOTTOM)


#Alright I understand what it does for the most part now.  
def time():
   string = strftime('%H:%M:%S %p')
   mark.config(text = string)
   mark.after(1000, time)

mark = Label(root,
   font = ('calibri', 40, 'bold'),
   pady=150,
   foreground = 'blue',
   background = 'pink')

mark.pack(anchor = 'center')
time()


#Code to play a fart sound if key combo is pressed
#Add If Else to check OS and run different code if it's on windows
#This only works on Linux/MacOS



#if keyboard.is_pressed('ctrl+f+a'):
 #     subprocess.call(["afplay", "fart.mp3"])

mainloop()