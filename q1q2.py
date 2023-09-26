class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle


vehicle = Vehicle('car', 200, 6000)
print(vehicle.name_of_vehicle)
print(vehicle.max_speed)
print(vehicle.average_of_vehicle)


class Car(Vehicle):
    def __init__(self):
        super().__init__('car', 200, 6000)

    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle}, capacity: {capacity}"


car = Car()
print(car.name_of_vehicle)
print(car.max_speed)
print(car.average_of_vehicle)
print(car.seating_capacity(5))
