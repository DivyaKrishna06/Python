class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.year} {self.make} {self.model}'s engine is now running.")

    def stop_engine(self):
        print(f"{self.year} {self.make} {self.model}'s engine has been stopped.")


class Bus(Vehicle):
    def __init__(self, make, model, year, passenger_capacity):
        # Call the constructor of the parent class (Vehicle) to initialize its attributes.
        super().__init__(make, model, year)
        self.passenger_capacity = passenger_capacity

    def announce_passenger_capacity(self):
        print(f"This bus can carry up to {self.passenger_capacity} passengers.")


# Example usage:
my_bus = Bus("Toyota", "Coaster", 2023, 20)
my_bus.start_engine()
my_bus.announce_passenger_capacity()
my_bus.stop_engine()