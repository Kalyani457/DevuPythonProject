def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 400 == 0):
        return True
    else:
        return False
year=int(input("Enter year to check leap year or not: "))
if is_leap_year(year):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")