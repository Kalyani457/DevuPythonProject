def Triangle(height, base, side1, sameside):
    if sameside == "Yes":
        side2 = side1
    else:
        side2 = int(input("Enter the second size: "))
    perimeter = base + side1 + side2
    area = 1/2 *  base * height
    return perimeter, area
    
height = int(input("Enter the Height of a triangle: "))
base = int(input("Enter the Base of a triangle: "))
side1 = int(input("Enter the side of a triangle: "))
sameside = input("Are both the sides of the same size?, Yes/No: ")

value = Triangle(height, base, side1, sameside)
print(f"Perimeter and Area of the triangle is: {value[0]}, {value[1]}")

def square(S1):
    area = 2 * S1
    perimeter = 4 * S1
    return area, perimeter

S1=int(input("Enter any side of the Square:"))
#square(S1)
print("Area and Perimeter of a Square is:", square(S1))

def rectangle(l,b):

    area = l * b
    perimeter = 2 * (l+b)
    return area, perimeter

l = int(input("Enter length of the rectangle:"))
b = int(input("Enter breadth of the rectangle:"))

#rectangle(l,b)
print("Area & perimeter of the rectangle is", rectangle(l,b))