class Car:
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model


class Dealership:
    def __init__(self):
        self.cars = ["Ford Fusion", "Honda Civic", "Dodge Dakota"]

    def __iter__(self):
        yield from self.cars

    def add_car(self, car):
        self.cars.append(car)
        

car_one = Car("Ford", "Mustang", 2020)
car_two = Car("Chevy", "Corvette", 2018)
car_three = Car("Chevy", "Cobalt", 2001)

dealership = Dealership()

