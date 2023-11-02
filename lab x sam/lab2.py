class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def drive(self):
        print(f"Driving the{self.make} {self.model}")
my_car = Car("Toyota", "Corolla")
my_car.drive()