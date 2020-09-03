def number(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
        #print(f"{n1} is Max number")

    elif n2 > n3:
        return n2
        #print(f"{n2} is Max number")
    
    else:
        return n3
        #print(f"{n3} is Max number")

n1=int(input("Enter first number:" ))
n2=int(input("Enter second number:" ))
n3=int(input("Enter third number:" ))
print(f"maximum number of {n1}, {n2}, {n3} is:", number(n1, n2, n3))