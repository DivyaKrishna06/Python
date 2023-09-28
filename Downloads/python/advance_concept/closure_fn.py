def outer_function(x):
    # This inner_function is a closure because it "closes over" the variable x
    def inner_function(y):
        return x + y
    return inner_function

# Create closures by calling outer_function with different values
closure1 = outer_function(10)
closure2 = outer_function(20)

# Check if the closures have __closure__ attribute
if hasattr(closure1, '__closure__') and hasattr(closure2, '__closure__'):
    # Print the values of the 'x' variable captured by each closure
    print("Closure 1 captures x =", closure1.__closure__[0].cell_contents)
    print("Closure 2 captures x =", closure2.__closure__[0].cell_contents)

# Call the closures with different 'y' values
result1 = closure1(5)
result2 = closure2(5)

# Print the results
print("Result 1 =", result1)
print("Result 2 =", result2)