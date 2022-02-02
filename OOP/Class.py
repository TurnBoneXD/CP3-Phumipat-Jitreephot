class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastName+"'s cart")

customer1 = Customer()
customer1.name = "Phumipat"
customer1.lastName = "Jitreephot"
customer1.age = "16"
customer1.addCart()

customer2 = Customer()
customer2.name = "Jittawat"
customer2.lastName = "Pinyosanit"
customer2.age = "17"
customer2.addCart()

customer3 = Customer()
customer3.name = "Aiyapat"
customer3.lastName = "Vorasaran"
customer3.age = "16"
customer3.addCart()

