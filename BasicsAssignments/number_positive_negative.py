def num(x):
    
    if x > 0:
        print(f"{x} is a positive integer")
    elif x==0:
        print("It is Zero")
    else:
        print(f"{x} is a negative number")

x=int(input("Enter any number: "))
num(x)
