def PowTwoGen(max_value=0):
    n = 0
    while n < max_value:
        yield 2 ** n
        n += 1

# Example usage:
max_value = 5  # Change this value to the maximum power of 2 you want to generate
power_of_two_generator = PowTwoGen(max_value)

for value in power_of_two_generator:
    print(value)