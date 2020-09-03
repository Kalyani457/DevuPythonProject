def quadrant(x, y):
    if x > 0 and y > 0:
        print(f"{x} and {y} lies in first quadrant")
    elif x < 0 and y > 0:
        print(f"{x} and {y} lies in second quadrant")
    elif x > 0 and y < 0:
        print(f"{x} and {y} lies in third quadrant")
    elif x < 0 and y < 0:
        print(f"{x} and {y} lies in 4th quadrant")
    else:
        print(f"{x} and {y} lies in origin")

x = float(input("Enter value for x-axis:"))
y = float(input("Enter value for y-axis:"))
quadrant(x, y)