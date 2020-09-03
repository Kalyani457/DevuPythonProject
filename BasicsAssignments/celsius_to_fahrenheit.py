#celsius*1.8 = fahrenheit - 32

def CtoF(C, F):
    
    Celsius = (F - 32) / (1.8)
    return Celsius

def FtoC(C, F):
    
    Fahrenheit = (C * 1.8) + 32
    return Fahrenheit

C = float(input("Enter temperature in Celsius: "))
F = float(input("Enter temperature in Farenheit: "))

print("Celsius to Fahrenheit is:", CtoF(C, F))
print("Fahrenheit to Celsius is:", FtoC(C, F))