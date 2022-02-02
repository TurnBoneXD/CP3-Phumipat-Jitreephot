#เปลี่ยนแปลงข้อมูลใน Tuple ไม่ได้ เหมาะใช้เก็บข้อมูลที่ไม่ได้เปลี่ยนแปลงบ่อยๆ

tuple1 = ("Alice", "Bob", "Trudy")
print(tuple1[:2])
print(tuple1[1:])
print(tuple1[1:3])  

tuple1 = ("Alice", "Bob", "Trudy")
tuple2 = ("Prame", "Guide")
tuple3 = tuple1 + tuple2
print(tuple3)
tuple4 = tuple1 * 2
print(tuple4) 

tuple1 = ("Alice", "Bob", "Trudy")
print("Alice" in tuple1)
print("Prame" in tuple1)   

tupleEx = (1, 2, 199, 4, 5)
print(len(tupleEx))     # แสดงจำนวนข้อมูลใน tuple
print(max(tupleEx))     # แสดงข้อมูลที่มากที่สุดใน tuple
print(min(tupleEx))     # แสดงข้อมูลที่น้อยที่สุดใน tuple
print(tupleEx.index(199))   # แสดงตำแหน่งของข้อมูลภายใร tuple    

#แปลง list tuple / tuple list 
list1 = [5, 6, 7, 8]
print(list1)
tuple1 = tuple(list1)
print(tuple1)

tupleEx = (1, 2, 199, 4, 5)
print(tupleEx)
listEx = list(tupleEx)
print(listEx)  
