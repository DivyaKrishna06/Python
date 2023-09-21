import math

# Input the coordinates of the two points
x1 = float(input("Enter the x-coordinate of point 1: "))
y1 = float(input("Enter the y-coordinate of point 1: "))
x2 = float(input("Enter the x-coordinate of point 2: "))
y2 = float(input("Enter the y-coordinate of point 2: "))

# Calculate the distance using the distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Print the result
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")
