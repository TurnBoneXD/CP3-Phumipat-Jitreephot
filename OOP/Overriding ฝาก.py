
class Animal():
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    name = "" #ใช้ __ หน้าตัวแปรเพื่อปกปิดข้อมูล (__name)
    def setName(self,text):
        self.name = text
        print("Setting New Cat Name = ", self.name)

    def eat(self):
        print("Meow !!", self.name)

cat1 = Cat()
cat1.setName("TT")
cat1.eat()

#โปรแกรมคำนวณเกรด(โรงเรียนเซนต์คาเบรียล) เพื่อนำข้อมูลไปประกอบการตัดสินใจเลือกเข้าคณะในอนาคต
#โปรแกรมนี้พัฒนาโดย นาย ภูมิภัทร จิตรีโภชน์




