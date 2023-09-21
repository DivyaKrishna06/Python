class Vehicle:
    pass

class School_bus(Vehicle):
    pass

# Create an instance of the School_bus class
school_bus = School_bus()

# Check if school_bus is an instance of the Vehicle class
if isinstance(school_bus, Vehicle):
    print("school_bus is an instance of the Vehicle class")
else:
    print("school_bus is not an instance of the Vehicle class")