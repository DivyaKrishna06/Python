# importing two file from package

from mypackage.mysubpackage import multiply_module
from mypackage import add_module, greet_module

print(greet_module.greet())
result = add_module.add(5, 3)
print(f"Addition 5+3= {result}")

product= multiply_module.multiply(4, 6)
print(f"Multiplication 4 x 6 = {product}")