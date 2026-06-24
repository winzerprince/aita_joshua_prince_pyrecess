# Define ojbect level attributes
# Atleast 2 methods
#


class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model, year):
        # Object level attributes
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine has started."

    def stop_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine has stopped."


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

print(car1.start_engine())
