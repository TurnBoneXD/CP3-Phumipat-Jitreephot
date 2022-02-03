
'''
grade_goal5 = int(input("กรอกเป้าหมาย GPAX 5 เทอม (Ex. 2.25,3.50) : "))
grade_goal6 = int(input("กรอกเป้าหมาย GPAX 6 เทอม (Ex. 2.25,3.50) : "))
'''

def science(): #วิทย์
    global wx_science
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai = float(input("ภาษาไทยพื้นฐาน : "))
    thai = float(input_grade_thai*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economics = float(input("เศรษฐศาสตร์ : "))
    economics = float(input_grade_economics*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art_music = float(input("ศิลปะ/ดนตรี : "))
    art_music = float(input_grade_art_music*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_math = float(input("คณิตศาสตร์ : "))
    math = float(input_grade_math*1.5)
    input_grade_physics = float(input("วิทยาศาสตร์ (ฟิสิกส์) : "))
    physics = float(input_grade_physics*1.5)
    input_grade_chemistry = float(input("วิทยาศาสตร์ (เคมี) : "))
    chemistry = float(input_grade_chemistry*1.5)
    input_grade_biology = float(input("วิทยาศาสตร์ (ชีวะ) : "))
    biology = float(input_grade_biology*1.5)
    input_grade_astronomy = float(input("โลก ดาราศาสตร์และอวกาศ : "))
    astronomy = float(input_grade_astronomy*1.0)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*1.0)

    #ผลรวม หนวยกิต*เกรด ของสายวิทย์
    wx_science = thai+math_ie+tech_design+sci_tech+social_ie+economics+pe1+art_music+techno+fun_eng+math+physics+chemistry+biology+astronomy+pe2+dev_eng


def amsp_science(): #วิทย์-ทั่วไป
    global wx_amsp_science
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เลือกเสรี)")
    input_grade_math_aptitude = float(input("ความถนัดทางคณิตศาสตร์ : "))
    math_aptitude = float(input_grade_math_aptitude*0.5)
    input_grade_extra_science = float(input("วิทยาศาสตร์เพิ่มพูน : "))
    extra_science = float(input_grade_extra_science*1.0)
    input_grade_english_for_test = float(input("ภาษาอังกฤษสำหรับข้อสอบวัดมาตรฐาน : "))
    english_for_test = float(input_grade_english_for_test*0.5)

    #ผลรวม หนวยกิต*เกรด ของสายวิทย์-ทั่วไป วิชาเสรี
    wx_amsp_science = math_aptitude+extra_science+english_for_test

def health_science(): #วิทย์-สุขภาพ
    global wx_health_science
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เลือกเสรี)")
    input_grade_math_aptitude = float(input("ความถนัดทางคณิตศาสตร์ : "))
    math_aptitude = float(input_grade_math_aptitude*0.5)
    input_grade_cell_bio_molecule = float(input("เซลล์/ชีววิทยาโมเลกุล : "))
    cell_bio_molecule = float(input_grade_cell_bio_molecule*1.0)
    input_grade_english_for_medical = float(input("ภาษาอังกฤษสำหรับวิทยาศาสตร์และการแพทย์ : "))
    english_for_medical = float(input_grade_english_for_medical*0.5)

    #ผลรวม หนวยกิต*เกรด ของสายวิทย์-สุขภาพ วิชาเสรี
    wx_health_science = math_aptitude+cell_bio_molecule+english_for_medical

def applied_science(): #วิทย์-ประยุกต์
    global wx_applied_science
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เลือกเสรี)")
    input_grade_math_aptitude = float(input("ความถนัดทางคณิตศาสตร์ : "))
    math_aptitude = float(input_grade_math_aptitude*0.5)
    input_grade_engineer_skill = float(input("ทักษะเชิงวิศวกรรม : "))
    engineer_skill = float(input_grade_engineer_skill*1.0)
    input_grade_english_for_test = float(input("ภาษาอังกฤษสำหรับข้อสอบวัดมาตรฐาน : "))
    english_for_test = float(input_grade_english_for_test*0.5)

    #ผลรวม หนวยกิต*เกรด ของสายวิทย์-ประยุกต์ วิชาเสรี
    wx_applied_science = math_aptitude+engineer_skill+english_for_test

def inter_science(): #วิทย์-อินเตอร์
    global wx_inter_science
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เลือกเสรี)")
    input_grade_sat_math = float(input("SAT MATH : "))
    sat_math = float(input_grade_sat_math*0.5)
    input_grade_advanced_science = float(input("SG Advanced Science : "))
    advanced_science = float(input_grade_advanced_science*0.5)
    input_grade_international_english = float(input("อังกฤษในแบบสอบวัดระดับนานาชาติ : "))
    international_english = float(input_grade_international_english*1.0)

    #ผลรวม หนวยกิต*เกรด ของสายวิทย์-อินเตอร์ วิชาเสรี
    wx_inter_science = sat_math+advanced_science+international_english

def smap(): #พสพ
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    
    







print('''
โปรแกรมนี้เป็นโปรแกรมที่จะนำข้อมูลเกรดของคุณไปคำนวณหา 
-GPAX 5,6 ภาคเรียน 
-คำนวณ GPA ตามกลุ่มสาระ
-คำนวณหาเกรดเฉลี่ยขั้นต่ำเพื่อบรรลุเป้าหมายเกรดที่ต้องการเมื่อจบการศึกษา
''')
print('''0 : สายการเรียน วิทยาศาสตร์-ทั่วไป")
1 : แผนการเรียน วิทยาศาสตร์-สุขภาพ
2 : แผนการเรียน วิทยาศาสตร์-ประยุกต์
3 : แผนการเรียน วิทยาศาสตร์-อินเตอร์
4 : แผนการเรียน สหศิลป์-จีน
5 : แผนการเรียน สหศิลป์-ญี่ปุ่น
6 : แผนการเรียน สหศิลป์-เยอรมัน
7 : แผนการเรียน สหศิลป์-การแสดง
8 : แผนการเรียน สหศิลป์-สังคม
9 : แผนการเรียน สหศิลป์-คำนวณ
''')

learning_path = input("พิมพ์ตัวเลข(1-9) เพื่อเลือกสายการเรียนของคุณ : ")



if learning_path == 1:
    print("")
    



