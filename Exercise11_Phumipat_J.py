num = int(input())
space = num-1
for i in range(num):
    print(" "*space,end = "",)
    print("*"*((i*2)+1))
    space -=1

