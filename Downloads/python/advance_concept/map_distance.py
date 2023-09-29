import math

# calculate the distance of a point from the origin
def distance_from_origin(point):
    x, y = point
    return math.sqrt(x**2 + y**2)

# points = [(1, 2), (3, 4), (0, 0), (5, 6), (7, 8)]
points = [ (4.5, 3), (2.1,-1), (6.8,-3), (1.4, 2.9) ]

distances = map(distance_from_origin, points) # map function to calculate distances for each point

max_distance = max(distances)

# Print the result
print("Maximum distance from the origin:", max_distance)