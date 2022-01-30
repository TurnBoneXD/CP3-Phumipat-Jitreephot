
userInput = int(input("Enter your favorite fruits :")) 
fruits = set()
while len(fruits) < userInput:
    fruits.add(input("Fruit :"))
    print(fruits)
