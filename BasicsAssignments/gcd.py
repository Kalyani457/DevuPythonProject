def GCD(x, y):
    i = 1
    while(i <= x and i <= y):
        if((x % i == 0) and (y % i == 0)):
            gcd = i 
        i = i + 1
    return gcd
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
print(f"GCD of {x} and {y} is:", GCD(x, y))