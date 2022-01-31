from tkinter import *
from tkinter import font


def SayHelloWorld():
    print("Hello World1")

def SayHelloWorld2():
    print("Hello World2")

def SayHelloWorld3():
    print("Hello World3")

mainWindow = Tk()
button = Button(mainWindow,text = "ClickMe1",command = SayHelloWorld).grid(row=1,column=1)
button2 = Button(mainWindow,text = "ClickMe2",command = SayHelloWorld2).grid(row=0,column=1)
button3 = Button(mainWindow,text = "ClickMe3",command = SayHelloWorld3).grid(row=1,column=0)
label = Label(mainWindow,text = "Hello World", width=20,fg="magenta",bg="#FFCC00",font=("Adobe Gothic Std B",16),anchor=E).grid(row=0,column=0)
#anchor W = ซ้าย / E = ขวา
mainWindow.mainloop()

