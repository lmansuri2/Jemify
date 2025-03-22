import tkinter
import os
import re
import sqlite3
from tkinter import *
import tkinter.messagebox
import sys


page = Tk()
page.title('Login Page')
page.geometry('350x440')

#user class
class user:
        def __init__(self, email, password):
                self.email = email
                self.password = password
        def validateEmail(self):
#Function that checks that entered email is valid
                emailAddress = self.email
                emailFormat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

                if emailAddress == (""):
            #checks if user has not entered their email in container
                       
                        return False

                elif re.fullmatch(emailFormat, emailAddress) == None:
     #checks if entered email address matches email pattern format       
                        
                        return False
                else:
                       return emailAddress
                        
            #If user has entered an email address and it is valid then email address is returned
        def validatePassword(self):
                password = self.password
                if len(password) < 6:
                       
                        return False 
                else:
                        return password       
        def compare(self):
                for i in range(0, len(storedEmail)):
                        if self.email == storedEmail:
                                if self.password == storedPass:
                                       return True
                                else:
                                        return False
                        elif self.email == "" or self.password == "":
                                empty = "empty"
                                return empty
                        elif i == len(storedEmail) - 1:
                               invalid = "invalid"
                               return invalid
                        else:
                         i = i + 1

#fetching data from user database

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
i = 0 #initial index
cursor.execute("SELECT emailAddress FROM UserData") #selects email address from table
storedEmail = cursor.fetchall()[i][i] #stores email address temporarily at that index
cursor.execute("SELECT password FROM UserData") #selects password from table 
storedPass = cursor.fetchall()[i][i] #stores password temporarily at that index
conn.commit() 
conn.close()

#function that checks if user inputs matches stored details in database
def signIn():
    userLogin = user(emailEntry.get(), passwordEntry.get())
    compareUser = userLogin.compare() #calling compare() from user class
    
    #if statement that produces the correct error message depending on issue with user inputs
    if compareUser == False: 
        tkinter.messagebox.showerror(message="Invalid email or password")  
    elif compareUser == "empty":
           tkinter.messagebox.showerror(message="Please make sure both fields have been filled in")  
    elif compareUser == "invalid":
            tkinter.messagebox.showerror(message="Account does not exist")  
    elif compareUser == True:
            os.system('createProject.py')


#runs register file when register button is clicked
def registerPage():
   os.system('register.py')
 
#creating the login widgets
loginLabel = tkinter.Label(page, text="Login")
emailLabel = tkinter.Label(page, text="Email")
emailEntry = tkinter.Entry(page)
passwordLabel = tkinter.Label(page, text="Password")
passwordEntry = tkinter.Entry(page, show='*')
loginButton = tkinter.Button(page, text="Sign in", command=signIn)
RegisterButton = tkinter.Button(page, text="Register", command=registerPage)

#placing login widgets on the screen
loginLabel.grid(row=0, column=0, columnspan=2)
RegisterButton.grid(row=0, column=0, columnspan=1 )
emailLabel.grid(row=2, column=0)
emailEntry.grid(row=2, column=1)
passwordLabel.grid(row=3, column=0)
passwordEntry.grid(row=3, column=1)
loginButton.grid(row=4, column=0, columnspan=2)

#run
page.mainloop()
