def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "Turbo" and passwordInput == "33628":
        print("Login success")
        return True
    else:
        print("Login failed")
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator():
    totalPrice = int(input("Total Price : "))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    result = price1 + price2
    return result

if login():
    showMenu()
    userSelected = menuSelect()
    if userSelected == 1:
        print(vatCalculator())
    elif userSelected == 2:
        print(priceCalculator())
    else:
        print("error")
