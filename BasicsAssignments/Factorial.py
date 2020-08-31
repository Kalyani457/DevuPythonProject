def factorial():
    if n<0:
        print("None")
    elif n<2:
        print("1")
    else:
        product=1
        for i in range(2,n+1):
            product=product*i
            print(product)
n=int(input("Enter any number:"))
factorial()