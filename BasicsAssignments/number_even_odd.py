def even_odd(n):
    
    if n%2 == 0:
        return True
        #print(f"{n} is an even number")
    else:
        return False
        #print(f"{n} is an odd number")

n = int(input("Enter number to check even or odd: "))
if even_odd(n):
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")
