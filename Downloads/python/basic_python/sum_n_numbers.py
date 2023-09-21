# Function to sum the first n positive integers using a loop
def sum_of_positive_integers(n):
    if n <= 0:
        return "n must be a positive integer"
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Input the value of n
n = int(input("Enter a positive integer n: "))

result = sum_of_positive_integers(n)
print(f"The sum of the first {n} positive integers is: {result}")
