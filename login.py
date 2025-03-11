import tkinter
import os
import re
import sqlite3
from tkinter import *
import tkinter.messagebox

page = Tk()
page.title('Login Page')
page.geometry('350x440')

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
                                        with open('createProject.py', 'r') as file: #opens register python file
                                                code = file.read() #reads code within the file
                                                exec(code)#executes/rules the python file when register button is clicked on
                                                quit(code)
                                        #had to quit or else page would keep loading even when exited
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
#fetching data
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
i = 0 #index
cursor.execute("SELECT emailAddress FROM UserData") 
storedEmail = cursor.fetchall()[i][i]
print(storedEmail) # to see the value stored in the variable in terminal
cursor.execute("SELECT password FROM UserData")
storedPass = cursor.fetchall()[i][i]
print(storedPass)
conn.commit()
conn.close()



def signIn():
    userLogin = user(emailEntry.get(), passwordEntry.get())
    email = userLogin.validateEmail()
    password = userLogin.validatePassword()
    compareUser = userLogin.compare() #calling compare() from user class
    #if statement that produces the correct error message depending on issue with user inputs
    if compareUser == False: 
        tkinter.messagebox.showerror(message="Invalid email or password")  
    elif compareUser == "empty":
           tkinter.messagebox.showerror(message="Please make sure both fields have been filled in")  
    elif compareUser == "invalid":
            tkinter.messagebox.showerror(message="Account does not exist")  




def registerPage():
    with open('register.py', 'r') as file: #opens register python file
        code = file.read() #reads code within the file
        exec(code) #executes/rules the python file when register button is clicked on

#creating the login widgets
loginLabel = tkinter.Label(page, text="Login")
emailLabel = tkinter.Label(page, text="Email")
emailEntry = tkinter.Entry(page)
passwordLabel = tkinter.Label(page, text="Password")
passwordEntry = tkinter.Entry(page, show="*")
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


page.mainloop()
