def is_number_prime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        return True
    
n = int(input("Enter any integer number: "))
if is_number_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")