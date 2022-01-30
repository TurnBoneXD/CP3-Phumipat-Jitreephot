systemMenu = {"ข้าวมันไก่":40,"ข้าวหมกไก่":55,"ต้มยำกุ้ง":50,"ข้าวขาหมู":45,}
menuList = []

def showBill():
    totalPrice = 0
    print("==== My Food ====")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1],"บาท")
        totalPrice += int(menuList[number][1])
    print("Total :",totalPrice,"บาท")

while True:
    menuName = input("Please enter menu : ")
    print(systemMenu[menuName],"บาท")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()









