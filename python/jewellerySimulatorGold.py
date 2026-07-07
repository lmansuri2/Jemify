import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab
from PIL import *
import tkinter.messagebox 

window = Tk()
window.title("Jemify")

#initial empty list used in stack used for undo function
list = []

#setting jewelleryMenu as the menu of Jemify application
jewelleryMenu = Menu(window)
window.config(menu=jewelleryMenu)
#save project function
def saveProject():
    fileName = "jewelleryDesign.png"
    x= window.winfo_rootx() + jewelleryCanvas.winfo_x() + 150 #retrieves coordinates of jewellery canvas
    y= window.winfo_rooty() + jewelleryCanvas.winfo_y() + 10 
    x1= x + jewelleryCanvas.winfo_width() + 400
    y1= y + jewelleryCanvas.winfo_height() + 200
    ImageGrab.grab().crop((x,y,x1,y1)).save(fileName) #saves jewellery canvas in created file name

fileMenu = Menu(window, tearoff=0) #tearoff is a default tab so to remove set equal it to 0

#menu tab that is displayed under File menu tab
jewelleryMenu.add_cascade(label="File", menu=fileMenu) #heading menu tab
fileMenu.add_command(label="Save...", command=saveProject) #save menu item

#import bead and charm image
charm = Image.open(r"C:\Users\user\Documents\jemifyProject\Jemify\images\flowerCharm.webp")
bead = Image.open(r"C:\Users\user\Documents\jemifyProject\Jemify\images\pearl.jpg")

#import gold jewellery image
jewellery = Image.open(r"C:\Users\user\Documents\jemifyProject\Jemify\images\GoldDropEarrings.png")

#resizing images
resizedJewellery = jewellery.resize((500, 400))
jewelleryNew = ImageTk.PhotoImage(resizedJewellery)

resizedCharm = charm.resize((50, 50))
charmNew = ImageTk.PhotoImage(resizedCharm)

resizedBead = bead.resize((50, 50))
beadNew = ImageTk.PhotoImage(resizedBead)

#canvas
jewelleryCanvas = Canvas(window, bg="red", height=370, width=493)
jewelleryCanvas.pack(pady=20)

#gold jewellery template
backgroundJewellery = jewelleryCanvas.create_image(250, 180, image=jewelleryNew)

#adding bead/charm onto canvas
def beadonCanvas():
    global createBead1, createBead2
    createBead1 = jewelleryCanvas.create_image(199, 245, image=beadNew)
    createBead2 = jewelleryCanvas.create_image(336, 245, image=beadNew)
    print(list)
    list.append(2) #different values to distinguish between charm and bead
    return list
    
def charmonCanvas():
    global createCharm1, createCharm2
    createCharm1 = jewelleryCanvas.create_image(199, 245, image=charmNew)
    createCharm2 = jewelleryCanvas.create_image(336, 245, image=charmNew)
    print(list)
    list.append(4)
    return list #returns list to be used in undo function


#bead and charm buttons

beadButton = ttk.Button(window, text="Pearl", image = beadNew, command= lambda: [beadonCanvas()])
beadButton.pack()
beadButton.place(x=600, y=450)

charmButton = ttk.Button(window, text="Charm", image = charmNew, command= lambda: [charmonCanvas()])
charmButton.pack()
charmButton.place(x=520, y=450)


#tools
class Tools:
    def __init__(self, icon):
        self.icon = icon
    def isEmpty(self):
        if len(list) == 0:
            tkinter.messagebox.showerror(title= self.icon + " list is empty", 
                                         message="Previous action is empty, nothing to be removed.")
            return True
        else:
            return False
    
    def isFull(self):
        global list
        if len(list) == 5:
            tkinter.messagebox.showerror(title= self.icon + " list is full", 
                                         message="Max number of " + self.icon +"'s reached")         
            return True
        else:
            return False

#undo image
undoIcon = Image.open(r"C:\Users\user\OneDrive\Dokumenty\Jewellery Simulator\jewelleryImages\undoIcon.webp")
undoIcon1 = ImageTk.PhotoImage(undoIcon)
resizedIcon = undoIcon.resize((50,50))
undoIcon1 = ImageTk.PhotoImage(resizedIcon)


#undo object from Tools class
undoObject = Tools(icon="Undo")

#undo function
def undo():
    global list
    global createCharm1, createCharm2, createBead1, createBead2 #to be accessed in undo function
    undoObject.isEmpty()
    undoObject.isFull()
    i = 0
    if len(list) == 1 or len(list) == 0:
        if list[0] == 2: #if value corresponds to Bead
            jewelleryCanvas.moveto(createBead1, -100, 0) 
            jewelleryCanvas.moveto(createBead2, -100, 0)
            list.pop(0)   
        elif list[0] == 4: #value corresponds to Charm
            jewelleryCanvas.moveto(createCharm1, -100, 0)
            jewelleryCanvas.moveto(createCharm2, -100, 0)  
            list.pop(0)      
    elif list[i] > list[i+1]:
        createCharm1 = jewelleryCanvas.create_image(199, 245, image=charmNew)
        createCharm2 = jewelleryCanvas.create_image(336, 245, image=charmNew)
        list.pop(0)
    elif list[i] < list[i+1]:#checking what it is at the top of the stack
        createBead1 = jewelleryCanvas.create_image(199, 245, image=beadNew)
        createBead2 = jewelleryCanvas.create_image(336, 245, image=beadNew)
        list.pop(0) #removes it and reduces length of list by 1 so the next item is at the top


#undo button

undoButton = Button(window, text="undo", image=undoIcon1, command=undo)
undoButton.pack()
undoButton.place(x=400, y=450)

#run
window.mainloop()

