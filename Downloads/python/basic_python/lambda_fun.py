# x = lambda a, b : a * b
# print(x(5, 6))


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(8))

def multiply_with_unknown_number(number):
    # List of multipliers
    multipliers = [2, 3, 4, 5]

    # Iterate through the multipliers and print the result
    for multiplier in multipliers:
        result = number * multiplier
        print(f"{multiplier} times the number {number} = {result}")

number_to_multiply = int(input('Enter the number:'))
multiply_with_unknown_number(number_to_multiply)