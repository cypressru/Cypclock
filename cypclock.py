from tkinter import *
from time import strftime
import webbrowser
import random
#Adding random stuff for functionality, ask if you need
root = Tk()
root.geometry("420x420")
root.resizable(0,0)
root.title('Cypclock 0.2')
#Above code is rules relating to the shape, title, and other properties of the window it's self

#Adding Variables, can be numbers or strings
new = 1
url = "https://www.youtube.com/watch?v=Q44DA9-TH2o&list=PLLGIaswzK8nerfBww5vX312Bt2B5A24om"


#Adding commands, or something idk, to be called later. I don't fully understand how they work yet, but I know enough to write this.
def openwebrandomdeclassified():
   urls = ['https://www.butts.com', 'https://boob.com', 'https://ass.com']
   random_url = random.choice(urls)
   webbrowser.open(random_url)
def openweb():
   webbrowser.open(url,new=new)
def expand ():
   pass

# Create the drop-down menu
menu = Menu(root)

# Create the "File" menu with a command for the "Open" option
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="Open", command=openweb)

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

#korn_amv_button = Button(root,
 #                 text="Korn AMVs",
  #                command=openweb,
   #               font=("calibri", 24),
    #              fg="blue")
#korn_amv_button.pack(pady=100)



# clock code
Label(root,text = 'KillGod420', font = 'arial 20 bold').pack(side=BOTTOM)


#Past this is code I copied online, all I understand is we defined time. Above I called this defining a command, but that's 
# just me guessing based off of what I was able to do with it before. I don't really understand what's happening below, 
# I will have to read more into it tomorrow. I want to use this to draw a GUI option for an analogue clock eventually so 
# I won't be able to avoid learning what this does lol.  
def time():
   string = strftime('%H:%M:%S %p')
   mark.config(text = string)
   mark.after(1000, time)

mark = Label(root,
   font = ('calibri', 40, 'bold'),
   pady=150,
   foreground = 'blue')

mark.pack(anchor = 'center')
time()

mainloop()