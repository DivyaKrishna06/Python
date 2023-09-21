
# Import the entire module
import my_module

# Use functions and variables from the module
print(my_module.say_hello(input('Enter your name: ')))
print(my_module.pi_value)

# Create an instance of the class from the module
math_instance = my_module.MyMath()
print(math_instance.square(int(input('Enter the integer:'))))

# Import specific items from the module
from my_module import say_hello, pi_value

print(say_hello(input('Enter your name: ')))
print(pi_value)
