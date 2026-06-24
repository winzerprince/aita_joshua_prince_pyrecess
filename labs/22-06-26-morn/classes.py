class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("Dog sits")

    def roll_over(self):
        print("Dog rolls over")


dogsen = Dog("Lucas", 12)

dogsen.sit()
