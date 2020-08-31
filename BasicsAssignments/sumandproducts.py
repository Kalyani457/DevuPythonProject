# enter any integer and get the sum and product of the integer
a = int(input("Enter any number to get the sum and product of the digits: "))
temp=a
product=1
total=0
while(temp!=0):
    product=product*(temp%10)
    total=total+(temp%10)
    temp=int(temp/10)
print("Product of the digits of a number:", product)
print("Sum of the digits of the number:", total)