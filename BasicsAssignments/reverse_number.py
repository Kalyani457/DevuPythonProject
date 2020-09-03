def reverse_number(n):

    reversed = 0
    while(n > 0):
        rem = int(n % 10)
        reversed = reversed * 10 + rem
        n = int(n / 10)
    return reversed

n=int(input("Enter a number:"))
print(f"Reverse of {n} is:", reverse_number(n))