from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        print("Started")

    @abstractmethod
    def stop(self):
        print("Stopped")


class Car(Vehicle):
    def __init__(self, name):
        pass

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    car = Car("name")

    car.start()
    car.stop()
