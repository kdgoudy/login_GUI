from tkinter import *
from tkinter import messagebox

#define function to initiate login
def login():
    username = entry1.get()
    password = entry2.get()

    #Use if/elif statement to accept username and password conditions
    if (username=="" and password==""):
        messagebox.showinfo("", "Blank not allowed")

    elif (username=='Goudy4' and password=='admin'):
        messagebox.showinfo("" , "Login successful")

    else:
        messagebox.showinfo("", "Incorrect username and password")

#Code to create interface, give title, set size of box
root = Tk()
root.title('Login')
root.geometry('350x200')

global entry1
global entry2

Label(root, text="Username").place(x=20,y=20)
Label(root, text="Password").place(x=20,y=70)

entry1=Entry(root, bd=5)
entry1.place(x=140,y=20)

entry2=Entry(root, bd=5)
entry2.place(x=140, y=70)

#Create button
Button(root, text='Login', command=login, height=3, width=13, bd=6).place(x=100,y=120)

#User mainloop()
root.mainloop()
