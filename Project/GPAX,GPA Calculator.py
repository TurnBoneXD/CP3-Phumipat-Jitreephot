
#ดูว่าผู้ใช้มีข้อมูลเกรดของเทอมไหนบ้าง
present_grade = int(input("ตอนนี้ผู้ใช้งานมีเกรดทั้งหมดกี้ภาคเรียน : "))
print(''': มีเกรด 1 เทอม''')
print("ผู้ใช้งานมีเกรดของเทอมไหนแล้วบ้าง")


'''
grade_goal5 = int(input("กรอกเป้าหมาย GPAX 5 เทอม (Ex. 2.25,3.50) : "))
grade_goal6 = int(input("กรอกเป้าหมาย GPAX 6 เทอม (Ex. 2.25,3.50) : "))
'''


def science_m4(): 
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai = float(input("ภาษาไทยพื้นฐาน (ท32103) : "))
    thai = float(input_grade_thai*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. (ค32103) : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี (ว32109) : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. (ว32103) : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. (ส32105) : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economics = float(input("เศรษฐศาสตร์ (ส32106) : "))
    economics = float(input_grade_economics*1.0)
    input_grade_pe32103 = float(input("สุขศึกษาและพลศึกษา (พ32103) : "))
    pe32103 = float(input_grade_pe32103*0.5)
    input_grade_art_music = float(input("ศิลปะ/ดนตรี (ศ32103/ด32103) : "))
    art_music = float(input_grade_art_music*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. (ง32103) : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English (อ32103) : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_math = float(input("คณิตศาสตร์ (ค32203) : "))
    math = float(input_grade_math*1.5)
    input_grade_physics = float(input("ฟิสิกส์ (ว32203) : "))
    physics = float(input_grade_physics*1.5)
    input_grade_chemistry = float(input("เคมี (ว32223) : "))
    chemistry = float(input_grade_chemistry*1.5)
    input_grade_biology = float(input("ชีวะ (ว32243) : "))
    biology = float(input_grade_biology*1.5)
    input_grade_astronomy = float(input("โลก ดาราศาสตร์และอวกาศ (ว32263) : "))
    astronomy = float(input_grade_astronomy*1.0)
    input_grade_pe32203 = float(input("สุขศึกษาและพลศึกษา (พ32203) : "))
    pe32203 = float(input_grade_pe32203*0.5)
    input_grade_dev_eng = float(input("Developmental English (อ32203) : "))
    dev_eng = float(input_grade_dev_eng*1.0)

print('''
โปรแกรมนี้เป็นโปรแกรมที่จะนำข้อมูลเกรดของคุณไปคำนวณหา 
-GPAX 5,6 ภาคเรียน 
-คำนวณ GPA ตามกลุ่มสาระ
-คำนวณหาเกรดเฉลี่ยขั้นต่ำเพื่อบรรลุเป้าหมายเกรดที่ต้องการเมื่อจบการศึกษา
''')
print('''1 : สายการเรียน วิทยาศาสตร์-ทั่วไป")
2 : สายการเรียน วิทยาศาสตร์-สุขภาพ
3 : สายการเรียน วิทยาศาสตร์-วิศวะ
4 : สายการเรียน วิทยาศาสตร์-อินเตอร์
5 : สายการเรียน ศิลป์-จีน
6 : สายการเรียน ศิลป์-ญี่ปุ่น
7 : สายการเรียน ศิลป์-เยอรมัน
8 : สายการเรียน ศิลป์-การแสดง
9 : สายการเรียน ศิลป์-สังคม
''')

learning_path = input("พิมพ์ตัวเลข(1-9) เพื่อเลือกสายการเรียนของคุณ : ")



if learning_path == 1:
    print("")
    



