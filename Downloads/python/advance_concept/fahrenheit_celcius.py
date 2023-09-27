# Convert from fahrenheit to celcius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

fahrenheit_temperatures = input("Enter a list of Fahrenheit temperatures separated by spaces: ").split()

# Convert using list comprehension
celsius_temperatures = [fahrenheit_to_celsius(float(temp)) for temp in fahrenheit_temperatures]

# result
print("Fahrenheit Temperatures:", fahrenheit_temperatures)
print("Celsius Temperatures:", celsius_temperatures)