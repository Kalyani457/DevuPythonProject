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

def Square():
    Area=2 * S1
    Perimeter=4* S1
    print("Area and Perimeter of a Square is:", Area, Perimeter)
S1=int(input("Enter any side of the Square:"))

Square()

def rectangle():
    Area = length * breadth
    perimeter = 2 * (length+breadth)
    print("Area & perimeter of the rectangle is", Area, "&", perimeter)
length = int(input("Enter length of the rectangle:"))
breadth = int(input("Enter breadth of the rectangle:"))

rectangle()