def number_divisibility(x, y):
    
    if x % y == 0:
        return True
        #print(f"{x}is divisible by {y}")

    else:
        return False
        #print(f"{x} is not divisible by {y}")

x=float(input("Enter x value:"))
y=float(input("Enter y value:"))
if number_divisibility(x, y):
    print(f"{x} is divisible by {y}")
else:
    print(f"{x} is not divisible by {y}")