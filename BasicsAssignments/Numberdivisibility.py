def number_divisibility():
    if x%y==0:
        print(f"{x}is divisible by {y}")
    else:
        print(f"{x} is not divisible by {y}")

x=float(input("Enter divisible number:"))
y=float(input("Enter divisor:"))
number_divisibility()