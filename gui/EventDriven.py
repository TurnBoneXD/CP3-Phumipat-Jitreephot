from tkinter import *

def leftClickButton(event):
    print("Left Click")

def middleClickButton(event):
    print("Middle Click")    

def rightClickButton(event):
    print("Right Click")

def doubleClickButton(event):
    print("Double Click")

main = Tk()
button = Button(main, text = "My Button!!")
button.pack()
#https://www.python-course.eu/tkinter_events_binds.php
button.bind('<Button-1>',leftClickButton) #1เม้าซ้าย 2เม้ากลาง 3เม้าขวา
button.bind('<Button-2>',middleClickButton)
button.bind('<Button-3>',rightClickButton)
button.bind('<Double-1>',doubleClickButton)
main.mainloop()