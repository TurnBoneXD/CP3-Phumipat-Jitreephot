def amsp_science():
    global wx_amsp_science
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เลือกเสรี)")
    input_grade_math_aptitude = float(input("ความถนัดทางคณิตศาสตร์ (ค32207) : "))
    math_aptitude = float(input_grade_math_aptitude*0.5)
    input_grade_extra_science = float(input("วิทยาศาสตร์เพิ่มพูน (ว32227) : "))
    extra_science = float(input_grade_extra_science*1.0)
    input_grade_english_for_test = float(input("ภาษาอังกฤษสำหรับข้อสอบวัดมาตรฐาน (อ32208) : "))
    english_for_test = float(input_grade_english_for_test*0.5)

    #ผลรวม หนวยกิต*เกรด ของสายวิทยาศาสตร์ทั่วไป วิชาเสรี
    wx_amsp_science = math_aptitude+extra_science+english_for_test

amsp_science()
print(wx_amsp_science)




    

