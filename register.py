import tkinter
import os
import re
import tkinter.messagebox 
import sqlite3
from tkinter import *
import sys

page2 = Tk()
page2.title('Register Page')
page2.geometry('350x440')


#user class
class user:
        def __init__(self, email, password):
                self.email = email
                self.password = password        
        def validateEmail(self):#method that checks that entered email is valid

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
                #If user has entered an email address and
                #it is valid then email address is returned

        def validatePassword(self):
                password = self.password
                if len(password) < 6:
                       
                        return False 
                else:
                        return password
   


def signUp():
        newUser = user(emailEntry.get(), passwordEntry.get())
        email = newUser.validateEmail()
        password = newUser.validatePassword()

        if email == False or password == False:
                tkinter.messagebox.showerror(title="Invalid Email/Password", message="Please make sure your "
                " email address is in the correct format or password is at least 6 characters long") 
        else:
                #Create Table for users
                conn = sqlite3.connect('users.db') #below checks if userData table exists
                table_create_query = '''CREATE TABLE IF NOT EXISTS UserData 
                        (emailAddress VARCHAR, password CHAR(60))
                '''
                #code below creates a new table with fields if it 'users.db' with fields does not exist                
                conn.execute(table_create_query) 
                #Insert user data
                data_insert_query = '''INSERT INTO UserData (emailAddress, password) VALUES 
                (?, ?)''' 
                data_insert_tuple = (email, password) #insert user's details into correct fields

                cursor = conn.cursor()
                #creates a new table with fields stated above in database 'users.db'
                conn.execute(data_insert_query, data_insert_tuple)
                conn.commit() 
                #to ensure changes are made to the database when the user enters valid details

                conn.close() #close database
                tkinter.messagebox.showinfo(title="Account Created", message="Account has been "
                                                                        "successfully created")


#runs login file when login button is clicked
def loginPage():
        os.system('login.py')


#creating the register widgets
registerLabel = tkinter.Label(page2, text="Sign Up")
emailLabel = tkinter.Label(page2, text="Email")
emailEntry = tkinter.Entry(page2)
passwordLabel = tkinter.Label(page2, text="Password")
passwordEntry = tkinter.Entry(page2, show="*")
createAccountButton = tkinter.Button(page2, text="Create Account", command=signUp)
loginButton = tkinter.Button(page2, text="Login", command=loginPage)

#placing register widgets on the screen
registerLabel.grid(row=0, column=0, columnspan=2)
loginButton.grid(row=0, column=0, columnspan=1 )
emailLabel.grid(row=2, column=0)
emailEntry.grid(row=2, column=1)
passwordLabel.grid(row=3, column=0)
passwordEntry.grid(row=3, column=1)
createAccountButton.grid(row=4, column=0, columnspan=2)

#user object from user class
newUser = user(emailEntry.get(), passwordEntry.get())



#run
page2.mainloop()
