
class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""

    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle): #สืบทอดโดยใช้ class แม่ ถ้าจะเพิ่มเติมข้อมูลอะไร Ex.เพิ่ม face #ถ้าสืบทอดแล้ว แม้ใน class จะไม่มีคำสั่งอะไรเลย ก็ยังสามารถใช้ code ใน class แม่ได้(Vehicle)
    def sayHello(self): #ส่วนที่อยู่ใน class นี้ จะสโคปแค่ใน class ลูก
        print("Hello World")


class PickUp(Vehicle):
    def pickUpThings(self):
        print("Picking Up")

class Van(Vehicle):
    def LongCar(self):
        print("Long Car")

class EstateCar(Vehicle):
    def LuxuryCar(self):
        print("LuxuryCar")


car1 = Car()
if True:
    car1.turnOnAirConditioner()
    car1.sayHello()




