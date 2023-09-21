class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self):
        super().__init__(seating_capacity=50)  # Bus has a fixed seating capacity of 50

    def fare(self):
        base_fare = super().fare()  # Calculate the base fare using the parent class method
        maintenance_charge = 0.10 * base_fare  # Calculate the maintenance charge (10% of base fare)
        total_fare = base_fare + maintenance_charge  # Calculate the total fare
        return total_fare

# Create a Bus instance
bus = Bus()

# Calculate and print the fare for the bus
print(f"The total fare for the bus is ${bus.fare():.2f}")