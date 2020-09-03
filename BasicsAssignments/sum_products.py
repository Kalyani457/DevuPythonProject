# enter any integer and get the sum and product of the digits

def sum_product(n):
    temp = n
    product = 1
    total = 0
    while (temp !=0):
        product = product * (temp % 10)
        total = total + (temp % 10)
        temp = int(temp / 10)
    return product, total
    
n = int(input("Enter any number to get the sum and product of the digits: "))
print(f"Sum and product of the digits of {n}:", sum_product(n))