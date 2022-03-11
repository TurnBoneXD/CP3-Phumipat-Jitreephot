def science_m4(): #วิทย์ ม.4 เทอม 1,2
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

    gpax = round((thai+math_ie+tech_design+sci_tech+social_ie+economics+pe1+art_music+techno+fun_eng+math+physics+chemistry+biology+astronomy+pe2+dev_eng)/16.5,2)
    wx_science = physics+chemistry+biology+astronomy
    credit_science = 5.5
    wx_math = math+math_ie
    credit_math = 2.5
    wx_language = fun_eng+dev_eng
    credit_language = 2
    wx_thai = thai
    credit_thai = 1
    wx_social = social_ie+economics
    credit_social = 2
    wx_art = art_music
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def health_science(): #วิทย์-สุขภาพ ม.5,6 ห้อง 1 เทอม 1,2
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
    
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เลือกเสรี)")
    input_grade_math_aptitude = float(input("ความถนัดทางคณิตศาสตร์ : "))
    math_aptitude = float(input_grade_math_aptitude*0.5)
    input_grade_cell_bio_molecule = float(input("เซลล์/ชีววิทยาโมเลกุล : "))
    cell_bio_molecule = float(input_grade_cell_bio_molecule*1.0)
    input_grade_english_for_medical = float(input("ภาษาอังกฤษสำหรับวิทยาศาสตร์และการแพทย์ : "))
    english_for_medical = float(input_grade_english_for_medical*0.5)

    gpax = round((thai+math_ie+tech_design+sci_tech+social_ie+economics+pe1+art_music+techno+fun_eng+math+physics+chemistry+biology+astronomy+pe2+dev_eng+math_aptitude+cell_bio_molecule+english_for_medical)/18.5,2)
    wx_science = physics+chemistry+biology+astronomy+cell_bio_molecule
    credit_science = 6.5
    wx_math = math+math_ie+math_aptitude
    credit_math = 3
    wx_language = fun_eng+dev_eng+english_for_medical
    credit_language = 2.5
    wx_thai = thai
    credit_thai = 1
    wx_social = social_ie+economics
    credit_social = 2
    wx_art = art_music
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,
    "credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def applied_science(): #วิทย์-ประยุกต์ ม.5,6 ห้อง 2,3 เทอม 1,2
    
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
    
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เลือกเสรี)")
    input_grade_math_aptitude = float(input("ความถนัดทางคณิตศาสตร์ : "))
    math_aptitude = float(input_grade_math_aptitude*0.5)
    input_grade_engineer_skill = float(input("ทักษะเชิงวิศวกรรม : "))
    engineer_skill = float(input_grade_engineer_skill*1.0)
    input_grade_english_for_test = float(input("ภาษาอังกฤษสำหรับข้อสอบวัดมาตรฐาน : "))
    english_for_test = float(input_grade_english_for_test*0.5)

    gpax = round((physics+chemistry+biology+astronomy+engineer_skill+math+math_ie+math_aptitude+fun_eng+dev_eng+english_for_test+thai+social_ie+economics+art_music+pe1+pe2+tech_design+sci_tech+techno)/18.5,2)
    wx_science = physics+chemistry+biology+astronomy+engineer_skill
    credit_science = 6.5
    wx_math = math+math_ie+math_aptitude
    credit_math = 3
    wx_language = fun_eng+dev_eng+english_for_test
    credit_language = 2.5
    wx_thai = thai
    credit_thai = 1
    wx_social = social_ie+economics
    credit_social = 2
    wx_art = art_music
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,
    "credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def amsp_science(): #วิทย์-ทั่วไป ม.5,6 ห้อง 4 เทอม 1,2
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
    
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เลือกเสรี)")
    input_grade_math_aptitude = float(input("ความถนัดทางคณิตศาสตร์ : "))
    math_aptitude = float(input_grade_math_aptitude*0.5)
    input_grade_extra_science = float(input("วิทยาศาสตร์เพิ่มพูน : "))
    extra_science = float(input_grade_extra_science*1.0)
    input_grade_english_for_test = float(input("ภาษาอังกฤษสำหรับข้อสอบวัดมาตรฐาน : "))
    english_for_test = float(input_grade_english_for_test*0.5)

    gpax = round((thai+math_ie+tech_design+sci_tech+social_ie+economics+pe1+art_music+techno+fun_eng+math+physics+chemistry+biology+astronomy+pe2+dev_eng+math_aptitude+extra_science+english_for_test)/18.5,2)
    wx_science = physics+chemistry+biology+astronomy+extra_science
    credit_science = 6.5
    wx_math = math+math_ie+math_aptitude
    credit_math = 3
    wx_language = fun_eng+dev_eng+english_for_test
    credit_language = 2.5
    wx_thai = thai
    credit_thai = 1
    wx_social = social_ie+economics
    credit_social = 2                
    wx_art = art_music
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def inter_science(): #วิทย์-อินเตอร์ ม.5,6 ห้อง 5 เทอม 1,2
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
    
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เลือกเสรี)")
    input_grade_sat_math = float(input("SAT MATH : "))
    sat_math = float(input_grade_sat_math*0.5)
    input_grade_advanced_science = float(input("SG Advanced Science : "))
    advanced_science = float(input_grade_advanced_science*0.5)
    input_grade_international_english = float(input("อังกฤษในแบบสอบวัดระดับนานาชาติ : "))
    international_english = float(input_grade_international_english*1.0)

    gpax = round((thai+math_ie+tech_design+sci_tech+social_ie+economics+pe1+art_music+techno+fun_eng+math+physics+chemistry+biology+astronomy+pe2+dev_eng+sat_math+advanced_science+international_english)/18.5,2)
    wx_science = physics+chemistry+biology+astronomy+advanced_science
    credit_science = 6
    wx_math = math+math_ie+sat_math
    credit_math = 3
    wx_language = fun_eng+dev_eng+international_english
    credit_language = 3
    wx_thai = thai
    credit_thai = 1
    wx_social = social_ie+economics
    credit_social = 2                
    wx_art = art_music
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def art_m4_term1(): #ศิลป์ ม.4 เทอม 1 ห้อง 6,7 
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์ พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art_music = float(input("ศิลปะ/ดนตรี : "))
    art_music = float(input_grade_art_music*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_extra_math = float(input("คณิตศาสตร์เพิ่มเติม : "))
    extra_math = float(input_grade_extra_math*1.5)
    input_grade_thai_civilization = float(input("อารยธรรมไทย : "))
    thai_civilization = float(input_grade_thai_civilization*2.0)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+extra_math+fun_eng+dev_eng+thai1+thai2+social_ie+history+thai_civilization+art_music+pe1+pe2+tech_design+sci_tech+techno)/16,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie+extra_math
    credit_math = 2.5
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+thai2
    credit_thai = 3
    wx_social = social_ie+history+thai_civilization
    credit_social = 4
    wx_art = art_music
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def art_m4_term2(): #ศิลป์ ม.4 เทอม 2 ห้อง 6,7
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_civic_duty = float(input("หน้าที่พลเมือง : "))
    civic_duty = float(input_grade_civic_duty*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art_music = float(input("ศิลปะ/ดนตรี : "))
    art_music = float(input_grade_art_music*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_extra_math = float(input("คณิตศาสตร์เพิ่มเติม : "))
    extra_math = float(input_grade_extra_math*1.5)
    input_grade_sea_study = float(input("โลกเอเชียตะวันออกเฉียงใต้ศึกษา : "))
    sea_study = float(input_grade_sea_study*2.0)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+extra_math+fun_eng+dev_eng+thai1+thai2+social_ie+civic_duty+sea_study+art_music+pe1+pe2+tech_design+sci_tech+techno)/16,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie+extra_math
    credit_math = 2.5
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+thai2
    credit_thai = 3
    wx_social = social_ie+civic_duty+sea_study
    credit_social = 4
    wx_art = art_music
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def cal_art_term1(): #ศิลป์-คำนวณ ม.5 ม.6 ห้อง 6 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทย : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_math = float(input("คณิตศาสตร์ : "))
    math = float(input_grade_math*1.5)
    input_grade_history = float(input("ปริทัศน์ประวัติศาสตร์ : "))
    history = float(input_grade_history*2.0)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เสรี)")
    input_grade_thai_for_business = float(input("ภาษาไทยเพื่อกิจธุระทางวิชาชีพ : "))
    thai_for_business = float(input_grade_thai_for_business*0.5)
    input_grade_math_aptitude = float(input("ความถนัดทางคณิตศาสตร์ : "))
    math_aptitude = float(input_grade_math_aptitude*1.0)
    input_grade_english_for_test = float(input("ภาษาอังกฤษสำหรับข้อสอบวัดมาตรฐาน : "))
    english_for_test = float(input_grade_english_for_test*1.0)

    gpax = round((math_ie+math+math_aptitude+fun_eng+dev_eng+english_for_test+thai1+thai2+thai_for_business+social_ie+economy+history+pe1+pe2+tech_design+sci_tech+techno+art)/18.5,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie+math+math_aptitude
    credit_math = 3.5
    wx_language = fun_eng+dev_eng+english_for_test
    credit_language = 4
    wx_thai = thai1+thai2+thai_for_business
    credit_thai = 3.5
    wx_social = social_ie+economy+history
    credit_social = 4
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def cal_art_term2(): #ศิลป์-คำนวณ ม.5 ม.6 ห้อง 6 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทย : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economy1 = float(input("เศรษศาสตร์ : "))
    economy1 = float(input_grade_economy1*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_thai2 = float(input("ภาษาไทย : "))
    thai2 = float(input_grade_thai2*2.0)
    input_grade_math = float(input("คณิตศาสตร์ : "))
    math = float(input_grade_math*1.5)
    input_grade_economy2 = float(input("เศรษศาสตร์ : "))
    economy2 = float(input_grade_economy2*2.0)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เสรี)")
    input_grade_thai_for_business = float(input("ภาษาไทยเพื่อกิจธุระทางวิชาชีพ : "))
    thai_for_business = float(input_grade_thai_for_business*0.5)
    input_grade_math_aptitude = float(input("ความถนัดทางคณิตศาสตร์ : "))
    math_aptitude = float(input_grade_math_aptitude*1.0)
    input_grade_english_for_test = float(input("ภาษาอังกฤษสำหรับข้อสอบวัดมาตรฐาน : "))
    english_for_test = float(input_grade_english_for_test*1.0)

    gpax = round((math_ie+math+math_aptitude+fun_eng+dev_eng+english_for_test+thai1+thai2+thai_for_business+social_ie+economy1+economy2+pe1+pe2+tech_design+sci_tech+techno+art)/18.5,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie+math+math_aptitude
    credit_math = 3.5
    wx_language = fun_eng+dev_eng+english_for_test
    credit_language = 4
    wx_thai = thai1+thai2+thai_for_business
    credit_thai = 3.5
    wx_social = social_ie+economy1+economy2
    credit_social = 4
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def social_art_term1(): #ศิลป์-สังคม ม.5 ม.6 ห้อง 7 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทย : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economy1 = float(input("เศรษศาสตร์ : "))
    economy1 = float(input_grade_economy1*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_math = float(input("คณิตศาสตร์ : "))
    math = float(input_grade_math*1.5)
    input_grade_history = float(input("ปริทัศน์ประวัติศาสตร์ : "))
    history = float(input_grade_history*2.0)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เสรี)")
    input_grade_thai_for_business = float(input("ภาษาไทยเพื่อกิจธุระทางวิชาชีพ : "))
    thai_for_business = float(input_grade_thai_for_business*0.5)
    input_grade_social_human = float(input("มนุษย์กับสังคม : "))
    social_human = float(input_grade_social_human*1.0)
    input_grade_english_for_test = float(input("ภาษาอังกฤษสำหรับข้อสอบวัดมาตรฐาน : "))
    english_for_test = float(input_grade_english_for_test*1.0)

    gpax = round((math_ie+math+fun_eng+dev_eng+english_for_test+thai1+extra_thai2+thai_for_business+social_ie+economy1+history+social_human+pe1+pe2+tech_design+sci_tech+techno+art)/18.5,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie+math
    credit_math = 2.5
    wx_language = fun_eng+dev_eng+english_for_test
    credit_language = 4
    wx_thai = thai1+extra_thai2+thai_for_business
    credit_thai = 3.5
    wx_social = social_ie+economy1+history+social_human
    credit_social = 5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno}

def social_art_term2(): #ศิลป์-สังคม ม.5 ม.6 ห้อง 7 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทย : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economy1 = float(input("เศรษศาสตร์ : "))
    economy1 = float(input_grade_economy1*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_thai2 = float(input("ภาษาไทย : "))
    thai2 = float(input_grade_thai2*2.0)
    input_grade_math = float(input("คณิตศาสตร์ : "))
    math = float(input_grade_math*1.5)
    input_grade_economy2 = float(input("เศรษศาสตร์ : "))
    economy2 = float(input_grade_economy2*2.0)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม (เสรี)")
    input_grade_thai_for_business = float(input("ภาษาไทยเพื่อกิจธุระทางวิชาชีพ : "))
    thai_for_business = float(input_grade_thai_for_business*0.5)
    input_grade_religion = float(input("ศาสนาเปรียบเทียบ : "))
    religion = float(input_grade_religion*1.0)
    input_grade_english_for_test = float(input("ภาษาอังกฤษสำหรับข้อสอบวัดมาตรฐาน : "))
    english_for_test = float(input_grade_english_for_test*1.0)

    gpax = round((math_ie+math+fun_eng+dev_eng+english_for_test+thai1+thai2+thai_for_business+social_ie+economy1+economy2+religion+pe1+pe2+tech_design+sci_tech+techno+art)/18.5,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie+math
    credit_math = 2.5
    wx_language = fun_eng+dev_eng+english_for_test
    credit_language = 4
    wx_thai = thai1+thai2+thai_for_business
    credit_thai = 3.5
    wx_social = social_ie+economy1+economy2+religion
    credit_social = 5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def japanese_art_m4_term1(): #สหศิลป์-ญี่ปุ่น ม.4 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_thai_civilization = float(input("อารยธรรมไทย : "))
    thai_civilization = float(input_grade_thai_civilization*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_japan = float(input("ภาษาญี่ปุ่น : "))
    japan = float(input_grade_japan*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+japan+thai1+extra_thai2+social_ie+history+thai_civilization+pe1+pe2+tech_design+sci_tech+techno+art)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+japan
    credit_language = 6
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+history+thai_civilization
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 
    
def japanese_art_m4_term2(): #สหศิลป์-ญี่ปุ่น ม.4 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_civic_duty = float(input("หน้าที่พลเมือง : "))
    civic_duty = float(input_grade_civic_duty*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_sea_study = float(input("โลกเอเชี่ยตะวันออกเฉียงใต้ศึกษา : "))
    sea_study = float(input_grade_sea_study*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_japan = float(input("ภาษาญี่ปุ่น : "))
    japan = float(input_grade_japan*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+japan+thai1+extra_thai2+social_ie+civic_duty+sea_study+pe1+pe2+tech_design+sci_tech+techno+art)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+japan
    credit_language = 6
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+civic_duty+sea_study
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def japanese_art_m5m6_term1(): #สหศิลป์-ญี่ปุ่น ม.5,6 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_history2 = float(input("ปริทัศน์ประวัติศาสตร์ : "))
    history2 = float(input_grade_history2*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_japan = float(input("ภาษาญี่ปุ่น : "))
    japan = float(input_grade_japan*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_japan2 = float(input("ภาษาญี่ปุ่น : "))
    japan2 = float(input_grade_japan2*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+japan+japan2+thai1+extra_thai2+social_ie+economy+history2+pe1+pe2+tech_design+sci_tech+techno+art)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+japan+japan2
    credit_language = 7
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history2
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def japanese_art_m5m6_term2(): #สหศิลป์-ญี่ปุ่น ม.5,6 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์ พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_japan = float(input("ภาษาญี่ปุ่น : "))
    japan = float(input_grade_japan*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_japan2 = float(input("ภาษาญี่ปุ่น : "))
    japan2 = float(input_grade_japan2*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+japan+japan2+thai1+extra_thai2+social_ie+economy+history+pe1+pe2+tech_design+sci_tech+techno+art)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+japan+japan2
    credit_language = 7
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def chinese_art_m4_term1(): #สหศิลป์-จีน ม.4 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_thai_civilization = float(input("อารยธรรมไทย : "))
    thai_civilization = float(input_grade_thai_civilization*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_chinese = float(input("ภาษาจีน : "))
    chinese = float(input_grade_chinese*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+chinese+thai1+extra_thai2+social_ie+history+thai_civilization+pe1+pe2+tech_design+sci_tech+techno+art)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+chinese
    credit_language = 6
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+history+thai_civilization
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 
    
def chinese_art_m4_term2(): #สหศิลป์-จีน ม.4 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_civic_duty = float(input("หน้าที่พลเมือง : "))
    civic_duty = float(input_grade_civic_duty*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_sea_study = float(input("โลกเอเชี่ยตะวันออกเฉียงใต้ศึกษา : "))
    sea_study = float(input_grade_sea_study*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_chinese = float(input("ภาษาจีน : "))
    chinese = float(input_grade_chinese*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+chinese+thai1+extra_thai2+social_ie+civic_duty+sea_study+pe1+pe2+tech_design+sci_tech+techno+art)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+chinese
    credit_language = 6
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+civic_duty+sea_study
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def chinese_art_m5m6_term1(): #สหศิลป์-จีน ม.5,6 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_history2 = float(input("ปริทัศน์ประวัติศาสตร์ : "))
    history2 = float(input_grade_history2*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_chinese = float(input("ภาษาจีน : "))
    chinese = float(input_grade_chinese*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_chinese2 = float(input("ภาษาจีน : "))
    chinese2 = float(input_grade_chinese2*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+chinese+chinese2+thai1+extra_thai2+social_ie+economy+history2+pe1+pe2+tech_design+sci_tech+techno+art)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+chinese+chinese2
    credit_language = 7
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history2
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def chinese_art_m5m6_term2(): #สหศิลป์-จีน ม.5,6 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์ พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_chinese = float(input("ภาษาจีน : "))
    chinese = float(input_grade_chinese*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_chinese2 = float(input("ภาษาจีน : "))
    chinese2 = float(input_grade_chinese2*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+chinese+chinese2+thai1+extra_thai2+social_ie+economy+history+pe1+pe2+tech_design+sci_tech+techno+art)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+chinese+chinese2
    credit_language = 7
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def german_art_m4_term1(): #สหศิลป์-เยอรมัน ม.4 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_thai_civilization = float(input("อารยธรรมไทย : "))
    thai_civilization = float(input_grade_thai_civilization*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_german = float(input("ภาษาเยอรมัน : "))
    german = float(input_grade_german*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+german+thai1+extra_thai2+social_ie+history+thai_civilization+pe1+pe2+tech_design+sci_tech+techno+art)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+german
    credit_language = 6
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+history+thai_civilization
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 
    
def german_art_m4_term2(): #สหศิลป์-เยอรมัน ม.4 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_civic_duty = float(input("หน้าที่พลเมือง : "))
    civic_duty = float(input_grade_civic_duty*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_sea_study = float(input("โลกเอเชี่ยตะวันออกเฉียงใต้ศึกษา : "))
    sea_study = float(input_grade_sea_study*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_german = float(input("ภาษาเยอรมัน : "))
    german = float(input_grade_german*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+german+thai1+extra_thai2+social_ie+civic_duty+sea_study+pe1+pe2+tech_design+sci_tech+techno+art)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+german
    credit_language = 6
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+civic_duty+sea_study
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 
    
def german_art_m5m6_term1(): #สหศิลป์-เยอรมัน ม.5,6 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_history2 = float(input("ปริทัศน์ประวัติศาสตร์ : "))
    history2 = float(input_grade_history2*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_german = float(input("ภาษาเยอรมัน : "))
    german = float(input_grade_german*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)
    
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_german2 = float(input("ภาษาเยอรมัน : "))
    german2 = float(input_grade_german2*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+german+german2+thai1+extra_thai2+social_ie+economy+history2+pe1+pe2+tech_design+sci_tech+techno+art)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+german+german2
    credit_language = 7
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history2
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def german_art_m5m6_term2(): #สหศิลป์-เยอรมัน ม.5,6 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์ พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_german = float(input("ภาษาเยอรมัน : "))
    german = float(input_grade_german*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_german2 = float(input("ภาษาเยอรมัน : "))
    german2 = float(input_grade_german2*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+german2+german+thai1+extra_thai2+social_ie+economy+history+pe1+pe2+tech_design+sci_tech+techno+art)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng+german2+german
    credit_language = 7
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history
    credit_social = 3.5
    wx_art = art
    credit_art = 0.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def music_art_m4_term1(): #สหศิลป์-ดนตรี ม.4 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_thai_civilization = float(input("อารยธรรมไทย : "))
    thai_civilization = float(input_grade_thai_civilization*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_music = float(input("ดนตรี : "))
    music = float(input_grade_music*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+thai1+extra_thai2+social_ie+history+thai_civilization+pe1+pe2+tech_design+sci_tech+techno+art+music)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+history+thai_civilization
    credit_social = 3.5
    wx_art = art+music
    credit_art = 3.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 
    
def music_art_m4_term2(): #สหศิลป์-ดนตรี ม.4 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_civic_duty = float(input("หน้าที่พลเมือง : "))
    civic_duty = float(input_grade_civic_duty*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_sea_study = float(input("โลกเอเชี่ยตะวันออกเฉียงใต้ศึกษา : "))
    sea_study = float(input_grade_sea_study*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_music = float(input("ดนตรี : "))
    music = float(input_grade_music*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+thai1+extra_thai2+social_ie+civic_duty+sea_study+pe1+pe2+tech_design+sci_tech+techno+art+music)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+civic_duty+sea_study
    credit_social = 3.5
    wx_art = art+music
    credit_art = 3.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 
     
def music_art_m5m6_term1(): #สหศิลป์-ดนตรี ม.5,6 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_history2 = float(input("ปริทัศน์ประวัติศาสตร์ : "))
    history2 = float(input_grade_history2*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_music = float(input("ดนตรี : "))
    music = float(input_grade_music*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)
    
    
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_music2 = float(input("ดนตรี : "))
    music2 = float(input_grade_music2*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+thai1+extra_thai2+social_ie+economy+history2+pe1+pe2+tech_design+sci_tech+techno+art+music+music2)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history2
    credit_social = 3.5
    wx_art = art+music+music2
    credit_art = 4.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def music_art_m5m6_term2(): #สหศิลป์-ดนตรี ม.5,6 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์ พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_music = float(input("ดนตรี : "))
    music = float(input_grade_music*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)
    
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_music2 = float(input("ดนตรี : "))
    music2 = float(input_grade_music2*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+thai1+extra_thai2+social_ie+economy+history+pe1+pe2+tech_design+sci_tech+techno+art+music+music2)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history
    credit_social = 3.5
    wx_art = art+music+music2
    credit_art = 4.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def acting_art_m4_term1(): #สหศิลป์-การแสดง ม.4 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_thai_civilization = float(input("อารยธรรมไทย : "))
    thai_civilization = float(input_grade_thai_civilization*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_acting_art = float(input("ศิลปะ : "))
    acting_art = float(input_grade_acting_art*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+thai1+extra_thai2+social_ie+history+thai_civilization+pe1+pe2+tech_design+sci_tech+techno+art+acting_art)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+history+thai_civilization
    credit_social = 3.5
    wx_art = art+acting_art
    credit_art = 3.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 
    
def acting_art_m4_term2(): #สหศิลป์-การแสดง ม.4 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_civic_duty = float(input("หน้าที่พลเมือง : "))
    civic_duty = float(input_grade_civic_duty*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_sea_study = float(input("โลกเอเชี่ยตะวันออกเฉียงใต้ศึกษา : "))
    sea_study = float(input_grade_sea_study*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_acting_art = float(input("ศิลปะ : "))
    acting_art = float(input_grade_acting_art*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)

    gpax = round((math_ie+fun_eng+dev_eng+thai1+extra_thai2+social_ie+civic_duty+sea_study+pe1+pe2+tech_design+sci_tech+techno+art+acting_art)/17,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+civic_duty+sea_study
    credit_social = 3.5
    wx_art = art+acting_art
    credit_art = 3.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 
     
def acting_art_m5m6_term1(): #สหศิลป์-การแสดง ม.5,6 ห้อง 8 เทอม 1
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_history2 = float(input("ปริทัศน์ประวัติศาสตร์ : "))
    history2 = float(input_grade_history2*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_acting_art = float(input("ศิลปะ : "))
    acting_art = float(input_grade_acting_art*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)
    
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_acting_art = float(input("ศิลปะ : "))
    acting_art2 = float(input_grade_acting_art*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+thai1+extra_thai2+social_ie+economy+history2+pe1+pe2+tech_design+sci_tech+techno+art+acting_art+acting_art2)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history2
    credit_social = 3.5
    wx_art = art+acting_art+acting_art2
    credit_art = 4.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 

def acting_art_m5m6_term2(): #สหศิลป์-การแสดง ม.5,6 ห้อง 8 เทอม 2
    print("กลุ่มสาระการเรียนรู้พื่นฐาน")
    input_grade_thai1 = float(input("ภาษาไทยพื้นฐาน : "))
    thai1 = float(input_grade_thai1*1.0)
    input_grade_math_ie = float(input("คณิตศาสตร์ IE. : "))
    math_ie = float(input_grade_math_ie*1.0)
    input_grade_tech_design = float(input("วิทยาการคำนวณ/การออกแบบเทคโนโลยี : "))
    tech_design = float(input_grade_tech_design*0.5)
    input_grade_sci_tech = float(input("วิทยาศาสตร์และเทคโนโลยี IE. : "))
    sci_tech = float(input_grade_sci_tech*1.0)
    input_grade_social_ie = float(input("สังคมศึกษา ศาสนา และวัฒนธรรม IE. : "))
    social_ie = float(input_grade_social_ie*1.0)
    input_grade_history = float(input("ประวัติศาสตร์ พื้นฐาน : "))
    history = float(input_grade_history*1.0)
    input_grade_pe1 = float(input("สุขศึกษา : "))
    pe1 = float(input_grade_pe1*0.5)
    input_grade_art = float(input("ศิลปะ : "))
    art = float(input_grade_art*0.5)
    input_grade_techno = float(input("การงานอาชีพ IE. : "))
    techno = float(input_grade_techno*0.5)
    input_grade_fun_eng = float(input("Fundamental English : "))
    fun_eng = float(input_grade_fun_eng*1.0)

    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_extra_thai2 = float(input("ภาษาไทยเพิ่มเติม : "))
    extra_thai2 = float(input_grade_extra_thai2*2.0)
    input_grade_economy = float(input("เศรษศาสตร์ : "))
    economy = float(input_grade_economy*1.5)
    input_grade_pe2 = float(input("พลศึกษา : "))
    pe2 = float(input_grade_pe2*0.5)
    input_grade_acting_art = float(input("ศิลปะ : "))
    acting_art = float(input_grade_acting_art*3.0)
    input_grade_dev_eng = float(input("Developmental English : "))
    dev_eng = float(input_grade_dev_eng*2.0)
    
    print("กลุ่มสาระการเรียนรู้เพิ่มเติม")
    input_grade_acting_art = float(input("ศิลปะ : "))
    acting_art2 = float(input_grade_acting_art*1.0)

    gpax = round((math_ie+fun_eng+dev_eng+thai1+extra_thai2+social_ie+economy+history+pe1+pe2+tech_design+sci_tech+techno+art+acting_art2+acting_art)/18,2)
    wx_science = 0
    credit_science = 0
    wx_math = math_ie
    credit_math = 1
    wx_language = fun_eng+dev_eng
    credit_language = 3
    wx_thai = thai1+extra_thai2
    credit_thai = 3
    wx_social = social_ie+economy+history
    credit_social = 3.5
    wx_art = art+acting_art2+acting_art
    credit_art = 4.5
    wx_pe = pe1+pe2
    credit_pe = 1
    wx_techno = tech_design+sci_tech+techno
    credit_techno = 2

    return {"gpax":gpax,
    "wx_science":wx_science,"credit_science":credit_science,
    "wx_math":wx_math,"credit_math":credit_math,
    "wx_language":wx_language,"credit_language":credit_language,
    "wx_thai":wx_thai,"credit_thai":credit_thai,
    "wx_social":wx_social,"credit_social":credit_social,
    "wx_art":wx_art,"credit_art":credit_art,
    "wx_pe":wx_pe,"credit_pe":credit_pe,
    "wx_techno":wx_techno,"credit_techno":credit_techno} 


q = "Y"
while q == "y" or q == "Y":
    print("""
    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
    """)

    #เก็บจำนวนเกรดของผู้ใช้งานที่มีลงในตัวแปร all_gpa
    print('''ตัวอย่างการใส่จำนวนเทอมที่มีเกรดเฉลี่ย 
    -มีใบเกรดตั้งแต่ ม.4 เทอม 1 ถึง ม.5 เทอม 1 (มีเกรดเฉลี่ยทั้งหมด 3 เทอม)
    -โปรแกรมจะไม่คำนวณเป้าหมายเกรดเฉลี่ย 5 เทอม หากผู้ใช้งานมีเกรดเฉลี่ย 5 หรือ 6 เทอมแล้ว
    -โปรแกรมจะไม่คำนวณเป้าหมายเกรดเฉลี่ย 6 เทอม หากผู้ใช้งานมีเกรดเฉลี่ย 6 เทอมแล้ว
    ''')
    useable_information = True
    while useable_information:
        all_gpa = int(input("ผู้ใช้งานมีเกรดเฉลี่ยทั้งหมดกี่เทอม (ถ้าไม่มีเลยให้ใส่เลข 0) : "))
        check_all_gpax = (0,1,2,3,4,5,6)
        if all_gpa not in check_all_gpax:
            print("โปรดใส่ข้อมูลให้ถูกต้อง (เลข 0 ถึง 6)")
        else:
            useable_information = False

    #เก็บเป้าหมายเกรด 5 เทอมลงในตัวแปร gpax_goal5
    if all_gpa != 5 and all_gpa != 6:
        useable_goal5 = True
        while useable_goal5:
            gpax_goal5 = float(input("เป้าหมายเกรดเฉลี่ยรวม 5 เทอม : "))
            if gpax_goal5 < 0 or gpax_goal5 > 4.00:
                print("โปรดใส่ข้อมูลให้ถูกต้อง")
            else:
                useable_goal5 = False


    #เก็บเป้าหมายเกรด 6 เทอมลงในตัวแปร gpax_goal6
    if all_gpa != 6:
        useable_goal6 = True
        while useable_goal6:
            gpax_goal6 = float(input("เป้าหมายเกรดเฉลี่ยรวม 6 เทอม : "))
            if gpax_goal6 < 0 or gpax_goal6 > 4.00:
                print("โปรดใส่ข้อมูลให้ถูกต้อง")
            else:
                useable_goal6 = False


    #เก็บข้อมูลสายการเรียนของผู้ใช้งานลงในตัวแปร learning_path
    print('''
    1 : แผนการเรียน วิทย์-สุขภาพ
    2 : แผนการเรียน วิทย์-ประยุกต์
    3 : แผนการเรียน วิทย์-ทั่วไป
    4 : แผนการเรียน วิทย์-อินเตอร์
    5 : แผนการเรียน สหศิลป์-คำนวณ
    6 : แผนการเรียน สหศิลป์-สังคม
    7 : แผนการเรียน สหศิลป์-จีน
    8 : แผนการเรียน สหศิลป์-ญี่ปุ่น
    9 : แผนการเรียน สหศิลป์-เยอรมัน
    10 : แผนการเรียน สหศิลป์-การแสดง
    11 : แผนการเรียน สหศิลป์-ดนตรี
    ''')
    useable_learning_path = True
    while useable_learning_path:
        learning_path = int(input("พิมพ์ตัวเลข(1-11) เพื่อเลือกสายการเรียน : "))
        check_learning_path = (1,2,3,4,5,6,7,8,9,10,11)
        if learning_path not in check_learning_path:
            print("โปรดใส่ข้อมูลให้ถูกต้อง (เลข 1 ถึง 11)")
        else:
            useable_learning_path = False

    user_information_list = []
    print("เทอมไหนที่ยังไม่มีเกรดเฉลี่ย ให้ทำการคาดคะเนเกรดของตนเอง")
    if learning_path == 1:
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(science_m4())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(science_m4())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(health_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(health_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(health_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(health_science())
    elif learning_path == 2:
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(science_m4())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(science_m4())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(applied_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(applied_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(applied_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(applied_science())
    elif learning_path == 3:
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(science_m4())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(science_m4())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(amsp_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(amsp_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(amsp_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(amsp_science())
    elif learning_path == 4:
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(science_m4())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(science_m4())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(inter_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(inter_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(inter_science())
        print("==============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(inter_science())
    elif learning_path == 5:
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(art_m4_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(art_m4_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(cal_art_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(cal_art_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(cal_art_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(cal_art_term2())
    elif learning_path == 6:
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(art_m4_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(art_m4_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(social_art_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(social_art_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(social_art_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(social_art_term2())
    elif learning_path == 7:
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(chinese_art_m4_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(chinese_art_m4_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(chinese_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(chinese_art_m5m6_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(chinese_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(chinese_art_m5m6_term2())
    elif learning_path == 8:
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(japanese_art_m4_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(japanese_art_m4_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(japanese_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(japanese_art_m5m6_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(japanese_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(japanese_art_m5m6_term2())
    elif learning_path == 9:
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(german_art_m4_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(german_art_m4_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(german_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(german_art_m5m6_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(german_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(german_art_m5m6_term2())
    elif learning_path == 10:
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(acting_art_m4_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(acting_art_m4_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(acting_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(acting_art_m5m6_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(acting_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(acting_art_m5m6_term2())
    elif learning_path == 11:
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 1")
        user_information_list.append(music_art_m4_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.4 เทอม 2")
        user_information_list.append(music_art_m4_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 1")
        user_information_list.append(music_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.5 เทอม 2")
        user_information_list.append(music_art_m5m6_term2())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 1")
        user_information_list.append(music_art_m5m6_term1())
        print("===============================================================")
        print(f"                กรอกข้อมูลเกรดเฉลี่ย ม.6 เทอม 2")
        user_information_list.append(music_art_m5m6_term2())
   
    #สรุปข้อมูลเกรดทุกเทอม  
    gpax41 = user_information_list[0]["gpax"]
    gpax42 = user_information_list[1]["gpax"]
    gpax51 = user_information_list[2]["gpax"]
    gpax52 = user_information_list[3]["gpax"]
    gpax61 = user_information_list[4]["gpax"]
    gpax62 = user_information_list[5]["gpax"]   

    #เก็บข้อมูลรอบ Portfolio
    total_gpax5 = round((gpax41+gpax42+gpax51+gpax52+gpax61)/5,2)
    total_gpax5 = "{:.2f}".format(total_gpax5)
    if all_gpa != 5 and all_gpa != 6:    
        grade5 = 0
        if all_gpa == 1:
            grade5 += gpax41
        elif all_gpa == 2:
            grade5 += gpax41+gpax42
        elif all_gpa == 3:
            grade5 += gpax41+gpax42+gpax51
        elif all_gpa == 4:
            grade5 += gpax41+gpax42+gpax51+gpax52
        goal5_complete = round( ( (gpax_goal5*5) - grade5 ) / (5-all_gpa),2)
        goal5_complete = "{:.2f}".format(goal5_complete)

    science_learing_path = (1,2,3,4)
    if learning_path in science_learing_path:
        wx_science5 = 0
        credit_science5 = 0
        for term in range(5):
            wx_science5 += user_information_list[term]["wx_science"]
            credit_science5 += user_information_list[term]["credit_science"]
        gpa_science5 = round(wx_science5/credit_science5,2)
        gpa_science5 = "{:.2f}".format(gpa_science5)

    wx_math5 = 0
    credit_math5 = 0
    for term in range(5):
        wx_math5 += user_information_list[term]["wx_math"]
        credit_math5 += user_information_list[term]["credit_math"]
    gpa_math5 = round(wx_math5/credit_math5,2)
    gpa_math5 = "{:.2f}".format(gpa_math5)

    wx_language5 = 0
    credit_language5 = 0
    for term in range(5):
        wx_language5 += user_information_list[term]["wx_language"]
        credit_language5 += user_information_list[term]["credit_language"]
    gpa_language5 = round(wx_language5/credit_language5,2)
    gpa_language5 = "{:.2f}".format(gpa_language5)

    wx_thai5 = 0
    credit_thai5 = 0
    for term in range(5):
        wx_thai5 += user_information_list[term]["wx_thai"]
        credit_thai5 += user_information_list[term]["credit_thai"]
    gpa_thai5 = round(wx_thai5/credit_thai5,2)
    gpa_thai5 = "{:.2f}".format(gpa_thai5)

    wx_social5 = 0
    credit_social5 = 0
    for term in range(5):
        wx_social5 += user_information_list[term]["wx_social"]
        credit_social5 += user_information_list[term]["credit_social"]
    gpa_social5 = round(wx_social5/credit_social5,2)
    gpa_social5 = "{:.2f}".format(gpa_social5)

    wx_art5 = 0
    credit_art5 = 0
    for term in range(5):
        wx_art5 += user_information_list[term]["wx_art"]
        credit_art5 += user_information_list[term]["credit_art"]
    gpa_art5 = round(wx_art5/credit_art5,2)
    gpa_art5 = "{:.2f}".format(gpa_art5)

    wx_pe5 = 0
    credit_pe5 = 0
    for term in range(5):
        wx_pe5 += user_information_list[term]["wx_pe"]
        credit_pe5 += user_information_list[term]["credit_pe"]
    gpa_pe5 = round(wx_pe5/credit_pe5,2)
    gpa_pe5 = "{:.2f}".format(gpa_pe5)

    wx_techno5 = 0
    credit_techno5 = 0
    for term in range(5):
        wx_techno5 += user_information_list[term]["wx_techno"]
        credit_techno5 += user_information_list[term]["credit_techno"]
    gpa_techno5 = round(wx_techno5/credit_techno5,2)
    gpa_techno5 = "{:.2f}".format(gpa_techno5)

    #เก็บข้อมูลรอบ Admission
    total_gpax6 = round((gpax41+gpax42+gpax51+gpax52+gpax61+gpax62)/6,2)
    total_gpax6 = "{:.2f}".format(total_gpax6)
    if all_gpa != 6:
        grade6 = 0
        if all_gpa == 1:
            grade6 += gpax41
        elif all_gpa == 2:
            grade6 += gpax41+gpax42
        elif all_gpa == 3:
            grade6 += gpax41+gpax42+gpax51
        elif all_gpa == 4:
            grade6 += gpax41+gpax42+gpax51+gpax52
        elif all_gpa == 5:
            grade6 += gpax41+gpax42+gpax51+gpax52+gpax61
        goal6_complete = round( ( (gpax_goal6*6) - grade6 ) / (6-all_gpa),2)
        goal6_complete = "{:.2f}".format(goal6_complete)

    science_learing_path = (1,2,3,4)
    if learning_path in science_learing_path:
        wx_science6 = 0
        credit_science6 = 0
        for term in range(6):
            wx_science6 += user_information_list[term]["wx_science"]
            credit_science6 += user_information_list[term]["credit_science"]
        gpa_science6 = round(wx_science6/credit_science6,2)
        gpa_science6 = "{:.2f}".format(gpa_science6)

    wx_math6 = 0
    credit_math6 = 0
    for term in range(6):
        wx_math6 += user_information_list[term]["wx_math"]
        credit_math6 += user_information_list[term]["credit_math"]
    gpa_math6 = round(wx_math6/credit_math6,2)
    gpa_math6 = "{:.2f}".format(gpa_math6)

    wx_language6 = 0
    credit_language6 = 0
    for term in range(6):
        wx_language6 += user_information_list[term]["wx_language"]
        credit_language6 += user_information_list[term]["credit_language"]
    gpa_language6 = round(wx_language6/credit_language6,2)
    gpa_language6 = "{:.2f}".format(gpa_language6)

    wx_thai6 = 0
    credit_thai6 = 0
    for term in range(6):
        wx_thai6 += user_information_list[term]["wx_thai"]
        credit_thai6 += user_information_list[term]["credit_thai"]
    gpa_thai6 = round(wx_thai6/credit_thai6,2)
    gpa_thai6 = "{:.2f}".format(gpa_thai6)

    wx_social6 = 0
    credit_social6 = 0
    for term in range(6):
        wx_social6 += user_information_list[term]["wx_social"]
        credit_social6 += user_information_list[term]["credit_social"]
    gpa_social6 = round(wx_social6/credit_social6,2)
    gpa_social6 = "{:.2f}".format(gpa_social6)

    wx_art6 = 0
    credit_art6 = 0
    for term in range(6):
        wx_art6 += user_information_list[term]["wx_art"]
        credit_art6 += user_information_list[term]["credit_art"]
    gpa_art6 = round(wx_art6/credit_art6,2)
    gpa_art6 = "{:.2f}".format(gpa_art6)

    wx_pe6 = 0
    credit_pe6 = 0
    for term in range(6):
        wx_pe6 += user_information_list[term]["wx_pe"]
        credit_pe6 += user_information_list[term]["credit_pe"]
    gpa_pe6 = round(wx_pe6/credit_pe6,2)
    gpa_pe6 = "{:.2f}".format(gpa_pe6)

    wx_techno6 = 0
    credit_techno6 = 0
    for term in range(6):
        wx_techno6 += user_information_list[term]["wx_techno"]
        credit_techno6 += user_information_list[term]["credit_techno"]
    gpa_techno6 = round(wx_techno6/credit_techno6,2)
    gpa_techno6 = "{:.2f}".format(gpa_techno6)

    if all_gpa != 5 and all_gpa != 6:
        if float(total_gpax5) >= float(gpax_goal5) :
            goal5_complete = f"({goal5_complete} (ตอนนี้เกรดของคุณถึงเป้าหมายแล้ว))"
        else:
            if  float(goal5_complete) <= 0 or  float(goal5_complete) > 4.00:
                goal5_complete = f"({goal5_complete} (เป็นไปไม่ได้แล้ว))"

    if all_gpa != 6:
        if float(total_gpax6) >= float(gpax_goal6):
            goal6_complete = f"({goal6_complete} (ตอนนี้เกรดของคุณถึงเป้าหมายแล้ว))"
        else:
            if  float(goal6_complete) <= 0 or  float(goal6_complete) > 4.00:
                goal6_complete = f"({goal6_complete} (เป็นไปไม่ได้แล้ว))"
    """ if all_gpa != 5 and all_gpa != 6:
        if float(total_gpax5) >= float(gpax_goal5) :
            goal5_complete = "(ตอนนี้เกรดของคุณถึงเป้าหมายแล้ว)"
        else:
            if  float(goal5_complete) <= 0 or  float(goal5_complete) > 4.00:
                goal5_complete = "(เป็นไปไม่ได้แล้ว)"

    if all_gpa != 6:
        if float(total_gpax6) >= float(gpax_goal6):
            goal6_complete = "(ตอนนี้เกรดของคุณถึงเป้าหมายแล้ว)"
        else:
            if  float(goal6_complete) <= 0 or  float(goal6_complete) > 4.00:
                goal6_complete = "(เป็นไปไม่ได้แล้ว)" """

    gpax_goal5 = "{:.2f}".format(gpax_goal5)
    gpax_goal6 = "{:.2f}".format(gpax_goal6)



    print("""

██╗░░░██╗░██████╗███████╗██████╗░
██║░░░██║██╔════╝██╔════╝██╔══██╗
██║░░░██║╚█████╗░█████╗░░██████╔╝
██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗
╚██████╔╝██████╔╝███████╗██║░░██║
░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝

██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
    """)

    print("=======================================================================")
    science_learing_path = (1,2,3,4)
    if learning_path in science_learing_path:
        gpa_left5 = 5-all_gpa
        output_science_portfolio = (0,1,2,3,4)
        if all_gpa in output_science_portfolio:
            print(f"""
    ข้อมูล 5 เทอม (รอบ Portfolio)
    เกรดเฉลี่ยรวม (GPAX) : {total_gpax5}
    เป้าหมายเกรดเฉลี่ยรวม 5 เทอม : {gpax_goal5}
    ค่าเฉลี่ยเกรดรวมอีก {gpa_left5} เทอม ต้องได้เกรดไม่ต่ำกว่า {goal5_complete}
    GPA วิทยาศาสตร์ : {gpa_science5}
    GPA คณิตศาสตร์ : {gpa_math5}
    GPA ภาษาต่างประเทศ : {gpa_language5}
    GPA ภาษาไทย : {gpa_thai5}
    GPA สังคมศึกษา : {gpa_social5}
    GPA ศิลปะ : {gpa_art5}
    GPA สุขศึกษาและพลศึกษา : {gpa_pe5}
    GPA การงานอาชีพและเทคโนโลยี : {gpa_techno5}

=======================================================================""")
        else:
            print(f"""
    ข้อมูล 5 เทอม (รอบ Portfolio)
    เกรดเฉลี่ยรวม (GPAX) : {total_gpax5}
    GPA วิทยาศาสตร์ : {gpa_science5}
    GPA คณิตศาสตร์ : {gpa_math5}
    GPA ภาษาต่างประเทศ : {gpa_language5}
    GPA ภาษาไทย : {gpa_thai5}
    GPA สังคมศึกษา : {gpa_social5}
    GPA ศิลปะ : {gpa_art5}
    GPA สุขศึกษาและพลศึกษา : {gpa_pe5}
    GPA การงานอาชีพและเทคโนโลยี : {gpa_techno5}

=======================================================================""")
        
        gpa_left6 = 6-all_gpa
        output_science_admission = (0,1,2,3,4,5)
        if all_gpa in output_science_admission:
            print(f"""
    ข้อมูล 6 เทอม (รอบ Admission)
    เกรดเฉลี่ยรวม (GPAX) : {total_gpax6}
    เป้าหมายเกรดเฉลี่ยรวม 6 เทอม : {gpax_goal6}
    คุณต้องมีเกรดเฉลี่ยรวมอีก {gpa_left6} เทอมที่เหลือไม่ต่ำกว่า {goal6_complete}
    GPA วิทยาศาสตร์ : {gpa_science6}
    GPA คณิตศาสตร์ : {gpa_math6}
    GPA ภาษาต่างประเทศ : {gpa_language6}
    GPA ภาษาไทย : {gpa_thai6}
    GPA สังคมศึกษา : {gpa_social6}
    GPA ศิลปะ : {gpa_art6}
    GPA สุขศึกษาและพลศึกษา : {gpa_pe6}
    GPA การงานอาชีพและเทคโนโลยี : {gpa_techno6}

=======================================================================""")
        else:
            print(f"""
    ข้อมูล 6 เทอม (รอบ Admission)
    เกรดเฉลี่ยรวม (GPAX) : {total_gpax6}
    GPA วิทยาศาสตร์ : {gpa_science6}
    GPA คณิตศาสตร์ : {gpa_math6}
    GPA ภาษาต่างประเทศ : {gpa_language6}
    GPA ภาษาไทย : {gpa_thai6}
    GPA สังคมศึกษา : {gpa_social6}
    GPA ศิลปะ : {gpa_art6}
    GPA สุขศึกษาและพลศึกษา : {gpa_pe6}
    GPA การงานอาชีพและเทคโนโลยี : {gpa_techno6}

=======================================================================""")

    elif learning_path not in science_learing_path:
        gpa_left5 = 5-all_gpa
        output_art_portfolio = (0,1,2,3,4)
        if all_gpa in output_art_portfolio:
            print(f"""
    ข้อมูล 5 เทอม (รอบ Portfolio)
    เกรดเฉลี่ยรวม (GPAX) : {total_gpax5}
    เป้าหมายเกรดเฉลี่ยรวม 5 เทอม : {gpax_goal5}
    ค่าเฉลี่ยเกรดรวมอีก {gpa_left5} เทอม ต้องได้เกรดไม่ต่ำกว่า {goal5_complete}
    GPA คณิตศาสตร์ : {gpa_math5}
    GPA ภาษาต่างประเทศ : {gpa_language5}
    GPA ภาษาไทย : {gpa_thai5}
    GPA สังคมศึกษา : {gpa_social5}
    GPA ศิลปะ : {gpa_art5}
    GPA สุขศึกษาและพลศึกษา : {gpa_pe5}
    GPA การงานอาชีพและเทคโนโลยี : {gpa_techno5}

=======================================================================""")
        else:
            print(f"""
    ข้อมูล 5 เทอม (รอบ Portfolio)
    เกรดเฉลี่ยรวม (GPAX) : {total_gpax5}
    GPA คณิตศาสตร์ : {gpa_math5}
    GPA ภาษาต่างประเทศ : {gpa_language5}
    GPA ภาษาไทย : {gpa_thai5}
    GPA สังคมศึกษา : {gpa_social5}
    GPA ศิลปะ : {gpa_art5}
    GPA สุขศึกษาและพลศึกษา : {gpa_pe5}
    GPA การงานอาชีพและเทคโนโลยี : {gpa_techno5}

=======================================================================""")
        
        gpa_left6 = 6-all_gpa
        output_art_admission = (0,1,2,3,4,5)
        if all_gpa in output_art_admission:
            print(f"""
    ข้อมูล 6 เทอม (รอบ Admission)
    เกรดเฉลี่ยรวม (GPAX) : {total_gpax6}
    เป้าหมายเกรดเฉลี่ยรวม 6 เทอม : {gpax_goal6}
    คุณต้องมีเกรดเฉลี่ยรวมอีก {gpa_left6} เทอมที่เหลือไม่ต่ำกว่า {goal6_complete}
    GPA คณิตศาสตร์ : {gpa_math6}
    GPA ภาษาต่างประเทศ : {gpa_language6}
    GPA ภาษาไทย : {gpa_thai6}
    GPA สังคมศึกษา : {gpa_social6}
    GPA ศิลปะ : {gpa_art6}
    GPA สุขศึกษาและพลศึกษา : {gpa_pe6}
    GPA การงานอาชีพและเทคโนโลยี : {gpa_techno6}

=======================================================================""")
        else:
            print(f"""
    ข้อมูล 6 เทอม (รอบ Admission)
    เกรดเฉลี่ยรวม (GPAX) : {total_gpax6}
    GPA คณิตศาสตร์ : {gpa_math6}
    GPA ภาษาต่างประเทศ : {gpa_language6}
    GPA ภาษาไทย : {gpa_thai6}
    GPA สังคมศึกษา : {gpa_social6}
    GPA ศิลปะ : {gpa_art6}
    GPA สุขศึกษาและพลศึกษา : {gpa_pe6}
    GPA การงานอาชีพและเทคโนโลยี : {gpa_techno6}

=======================================================================""")

    gpax41 = "{:.2f}".format(gpax41)
    gpax42 = "{:.2f}".format(gpax42)
    gpax51 = "{:.2f}".format(gpax51)
    gpax52 = "{:.2f}".format(gpax52)
    gpax61 = "{:.2f}".format(gpax61)
    gpax62 = "{:.2f}".format(gpax62)
    print(f"""
    เกรดเฉลี่ย ม.4 เทอม 1 : {gpax41}
    เกรดเฉลี่ย ม.4 เทอม 2 : {gpax42}
    เกรดเฉลี่ย ม.5 เทอม 1 : {gpax51}
    เกรดเฉลี่ย ม.5 เทอม 2 : {gpax52}
    เกรดเฉลี่ย ม.6 เทอม 1 : {gpax61}
    เกรดเฉลี่ย ม.6 เทอม 2 : {gpax62}""")

    if all_gpa != 0:
        print(f"""
    เกรด {int(all_gpa)} เทอมแรกของคุณ เป็นเกรดที่คุณมีข้อมูลอยู่แล้ว
    เกรดอีก {int(6-all_gpa)} เทอมที่เหลือ เป็นเกรดที่คุณคาดคะเนเอาไว้
    ซึ่งนั่นหมายความว่า คุณอาจจะไม่สามารถทำให้เกรดเป็นไปตามเป้าหมายได้
    หากไม่ทำให้เกรดของคุณเป็นไปตามที่คาดคะเนเอาไว้

=======================================================================""")
    else:
        print(f"""
    เกรดทั้งหมดเป็นเกรดที่คุณคาดคะเนเอาไว้
    ซึ่งนั่นหมายความว่า คุณอาจจะไม่สามารถทำให้เกรดเป็นไปตามเป้าหมายได้
    หากไม่ทำให้เกรดของคุณเป็นไปตามที่คาดคะเนเอาไว้

=======================================================================""")
    q = input("Repeat ? (Y/N) >>> ")
