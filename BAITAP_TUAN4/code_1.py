class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def print_details(self):
        print("Vehicle name:", self.name, "Max speed:", self.max_speed, "Mileage:", self.mileage)
        
    def print_capacity(self, capacity):
        if capacity:
            return f"The seating capacity of {self.name} is {capacity} passengers."

class Bus(Vehicle):
    def seating_capacity(self, capacity=29):
        return f"The seating capacity of {self.name} is {capacity} passengers."

class Car(Vehicle):
    def seating_capacity(self, capacity=4):
        return f"The seating capacity of {self.name} is {capacity} passengers."
    

    

b = Bus("Mercesben", 180, 12)
b.print_details()
print(b.seating_capacity())
c = Car("Vinfast", 160, 20)
c.print_details()
