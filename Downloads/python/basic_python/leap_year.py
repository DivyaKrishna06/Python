def is_leap_year(year):
    if (year % 4 == 0):
        return True
    else:
        return False

# Input year from the user
year = int(input("Enter a year: "))

# Call the function to check if it's a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")