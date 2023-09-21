class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"Max Speed: {self.max_speed} MPH")
        print(f"Mileage: {self.mileage} MPG")

# Create instances of the Vehicle class
car1 = Vehicle(120, 25)
car2 = Vehicle(150, 20)

# Display information about the vehicles
print("Vehicle 1:")
car1.display_info()

print("\nVehicle 2:")
car2.display_info()
