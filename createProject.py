import tkinter
import os
import re
import sqlite3
from tkinter import *
import tkinter.messagebox

page3 = Tk()
page3.title('Create Project')
page3.geometry('350x440')


#class jewellery that checks whether user has selected gold or silver
class jewellery:
    def __init__(self, metal):
        self.metal = metal
    def selectedMetal(self):
        if self.metal == "Gold":
            value = "Gold"
            return value
        elif self.metal == "Silver":
            value = "Silver"
            return value
        

def submit():
    #jewellery object that takes user input value used to load correct jewellery simulator
    option = jewellery(metalvar.get()) 
    userMetal = option.selectedMetal()
    if userMetal == "Gold":
        os.system('jewellerySimulatorGold.py')
        
    elif userMetal == "Silver":
        os.system('jewellerySimulatorSilver.py')
         
    else:
        tkinter.messagebox.showinfo(message="Only one option needs to be selected")
        #if both options have been selected

#variable is set because it's value will change depending on user selected metal
metalvar = tkinter.StringVar() 

#metal type options
earrings = tkinter.Label(page3, text="Select a metal to design earrings")
earrings.pack()

gold = tkinter.Radiobutton(page3, variable=metalvar, text="Gold", value="Gold")
gold.pack()

silver = tkinter.Radiobutton(page3, variable=metalvar, text="Silver", value = "Silver")
silver.pack()

submitButton = tkinter.Button(page3, text="Submit", command=submit)
submitButton.pack()


#run
page3.mainloop()
