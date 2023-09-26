# Multiple inheritance is when a class inherits from multiple parent classes, combining the
# characteristics (properties, methods) of all of them with its own properties and methods

class Car:
    def medium_of_transport(self):
        return 'Land'


class Boat:
    def medium_of_transport(self):
        return 'Water'


class Hovercraft(Car, Boat):
    def medium_of_transport(self):
        return 'Land/Water'


car = Car()
print(f"Car moves on {car.medium_of_transport()}")

boat = Boat()
print(f"Boat moves on {boat.medium_of_transport()}")

hovercraft = Hovercraft()
print(f"Hovercraft moves on {hovercraft.medium_of_transport()}")
