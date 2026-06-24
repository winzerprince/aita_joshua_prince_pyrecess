# The diamond problem is a problem that arises in object-oriented programming when a class inherits from two classes that have a common base class..
# This can lead to ambiguity in the method resolution order (MRO) and can cause unexpected behavior.
# This can be illustrated with the following example:
#


class A:
    def method(self):
        print("Method from class A")


class B(A):
    def method(self):
        print("Method from class B")


class C(A):
    def method(self):
        print("Method from class C")


class D(B, C):
    pass


d = D()

print(d.method())  # This will call the method from class B due to the MRO
print(D.__mro__)  # This will show the method resolution order
