import math

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the HCF using math.gcd()
hcf = math.gcd(num1, num2)

# Print the result
print(f"The HCF of {num1} and {num2} is {hcf}")
