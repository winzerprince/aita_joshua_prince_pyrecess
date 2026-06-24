# Inheritance and polymorphism
#


class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def info(self):
        return f"{self.name} is a {self.breed}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
        self.__help = "This is a dog class"
        self.name = name
        self.breed = breed

    def sound(self):
        print()


dog1 = Dog("Buddy", "Golden Retriever")

print(dog1.info())
print(dog1.breed)
