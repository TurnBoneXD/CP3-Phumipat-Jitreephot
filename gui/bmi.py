from tkinter import *
import math

topic30 = "อ้วนมาก (30.0 ขึ้นไป)"
info30 = "ค่อนข้างอันตราย เพราะเข้าเกณฑ์อ้วนมาก เสี่ยงต่อการเกิดโรคร้ายแรงที่แฝงมากับความอ้วน หากค่า BMI อยู่ในระดับนี้ จะต้องระวังการรับประทานไขมัน และควรออกกำลังกายอย่างสม่ำเสมอ"

topic25 = "อ้วน (25.0 - 29.9)"
info25 = "คุณอ้วนในระดับหนึ่ง ถึงแม้จะไม่ถึงเกณฑ์ที่ถือว่าอ้วนมาก ๆ แต่ก็ยังมีความเสี่ยงต่อการเกิดโรคที่มากับความอ้วนได้เช่นกัน ทั้งโรคเบาหวาน และความดันโลหิตสูง"

topic23 = "น้ำหนักเกิน (23.0 - 24.9)"
info23 = "พยายามอีกนิดเพื่อลดน้ำหนักให้เข้าสู่ค่ามาตรฐาน เพราะค่า BMI ในช่วงนี้ยังถือว่าเป็นกลุ่มผู้ที่มีความอ้วนอยู่บ้าง"

topic18 = "น้ำหนักปกติ เหมาะสม (18.6 - 22.9)"
topic18 = "น้ำหนักที่เหมาะสมสำหรับคนไทยคือค่า BMI ระหว่าง 18.5-22.9 จัดอยู่ในเกณฑ์ปกติ ห่างไกลโรคที่เกิดจากความอ้วน และมีความเสี่ยงต่อการเกิดโรคต่างๆน้อยที่สุด"

topic18l = "ผอมเกินไป (น้อยกว่า 18.5)"
info18l = "น้ำหนักน้อยกว่าปกติก็ไม่ค่อยดี หากคุณสูงมากแต่น้ำหนักน้อยเกินไป อาจเสี่ยงต่อการได้รับสารอาหารไม่เพียงพอหรือได้รับพลังงานไม่เพียงพอ ส่งผลให้ร่างกายอ่อนเพลียง่าย"



def bmiCalculate(event):
    bmi = (float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get())/100,2))
    labelBMI.configure(text = bmi)

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

labelBMI = Label(main,font=("Cordia New",16))
labelBMI.grid(row=2,column=1)

BMITopic = Label(main,text = "a",font=("Cordia New",18,"bold"),anchor = W)
BMITopic.grid(row=3,column=0)

BMIinfo = Label(main,text = "a",font=("Cordia New",16),anchor = W)
BMIinfo.grid(row=4,column=0)

main.mainloop()