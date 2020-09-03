def check_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False
    
a=int(input("Enter value a:"))
b=int(input("Enter value b:"))
c=int(input("Enter value c:"))
if check_triangle(a, b, c):
    print("triangle is possible")
else:
    print("triangle is not possible")