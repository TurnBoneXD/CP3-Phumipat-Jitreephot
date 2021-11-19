def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput  == "Turbo"  and passwordInput == "33628":
        return True
    else:
        return False
def menuProduct():
    pass
def selectedProduct():
    pass
def priceCalculate():
    pass

login()

'''
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput  == "Turbo"  and passwordInput == "33628":
    print("Done")  
    print("----- Weclome to TurnShop -----")    
    print("Type Letter to choose products")
    print("B","for Banana","    >>",20 ," THB per each")
    print("A","for Apple","     >>",50 ," THB per each")
    print("G","for Grape","     >>",80 ," THB per each")
    print("W","for Watermelon",">>",120 ,"THB per each")
    print("O","for Orange","    >>",15 ," THB per each")
    userSelectedProduct = str(input("Type Letter to choose product >> "))
    if userSelectedProduct == str("B"):
        userSelectedAmount = int(input("How much do you need ? >> "))
        print("Total Price >>",20*userSelectedAmount,"THB")
    elif userSelectedProduct == str("A"):
        userSelectedAmount = int(input("How much do you need ? >> "))
        print("Total Price >>",50*userSelectedAmount,"THB")
    elif userSelectedProduct == str("G"):
        userSelectedAmount = int(input("How much do you need ? >> "))
        print("Total Price >>",50*userSelectedAmount,"THB")
    elif userSelectedProduct == str("W"):
        userSelectedAmount = int(input("How much do you need ? >> "))
        print("Total Price >>",120*userSelectedAmount,"THB")
    elif userSelectedProduct == str("O"):
        userSelectedAmount = int(input("How much do you need ? >> "))
        print("Total Price >>",15*userSelectedAmount,"THB")
    else :
        print("We don't have that products")
else:
    print("Wrong username or password")
    print("Please try again")
'''      

