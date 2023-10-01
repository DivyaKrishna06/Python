import mymodule

name = "Alice"
greeting = mymodule.say_hello(name)
print(greeting)

radius = 5
area = mymodule.pi_value * mymodule.MyMath.square(radius)
print(f"The area of a circle with radius {radius} is {area}")