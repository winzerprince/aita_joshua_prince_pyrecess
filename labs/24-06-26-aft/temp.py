# What is polymorphism?
# Polymorphism is a concept in programming that allows objects of different classes to be treated as
# objects of a common superclass. It enables a single interface to represent different underlying forms
# (data types). In object-oriented programming, polymorphism allows methods to do different things based
# on the object it is acting upon, even if they share the same name.
#
# default arguments
# Varaible length arguments e.g *args, **kwargs
#
# In python
# 1. Default params

# Method overloading with default arguments, and variable length arguments
class Calculator:
    def add(self, a, b):
        return a + b

    #
    # def add(self, a, b=0):
    #     return a + b
    #
    # def add(self, *args):
    #     sum = 0
    #     for num in args:
    #         sum = sum + num
    #     return sum
    #


# Method overloading with type checking
#
class Calculato:
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b


# Method overriding
# Method overriding key points
# mehtod signature should be same
# Example


class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


# In the example above, the Dog class overrides the speak method of the Animal class. When we call
# the speak method on an instance of Dog, it will execute the overridden method in the Dog class,
# rather than the one in the Animal class.
