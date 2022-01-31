from tkinter import *
import math

topic30 = "อ้วนมาก"
topic25 = "อ้วน"
topic23 = "น้ำหนักเกิน"
topic18 = "น้ำหนักปกติ"
topic18l = "ผอมเกินไป"

def bmiCalculate(event):
    bmi = (float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get())/100,2))
    if bmi >= 30:
        labelBMI.configure(text = topic30)
    elif bmi >= 25.0 and bmi <= 29.9:
        labelBMI.configure(text = topic25)
    elif bmi >= 23.0 and bmi <= 24.9:
        labelBMI.configure(text = topic23)
    elif bmi >= 18.6 and bmi <= 22.9:
        labelBMI.configure(text = topic18)
    else:
        labelBMI.configure(text = topic18l)

main = Tk()
labelHeight = Label(main,text="ส่วนสูง(cm.)",font=("Cordia New",16))
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(main,text="น้ำหนัก(kg.)",font=("Cordia New",16))
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1,column=1)

buttonCal = Button(main, text = "คำนวณ",font=("Cordia New",16))
buttonCal.grid(row=2,column=0)
buttonCal.bind('<Button-1>',bmiCalculate)

labelBMI = Label(main,text="ผลลัพธ์",font=("Cordia New",16))
labelBMI.grid(row=2,column=1)


main.mainloop()