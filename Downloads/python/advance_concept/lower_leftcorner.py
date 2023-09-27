from functools import reduce

point_locations = [(1, 3), (2, 5), (-1, 4), (0, 2), (3, 1)]

def find_lower_left_corner(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    min_x = min(x1, x2)
    min_y = min(y1, y2)
    return (min_x, min_y)

lower_left_corner = reduce(find_lower_left_corner, point_locations)

print("Lower left corner:", lower_left_corner)