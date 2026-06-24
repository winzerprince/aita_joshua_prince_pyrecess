class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")
        super().show()


class C(A):
    def show(self):
        print("Class C")
        super().show()


class D(B, C):
    def show(self):
        print("Class D")
        super().show()
        super().show()
        super().show()


d = D()
print(d.show())  # This will call the method from class D, then B, then C, then A
print(D.__mro__)  # This will show the method resolution order
# Understand the super() doesn't always call the method from the immediate parent class, but rather
# follows the method resolution order (MRO) to determine which method to call next. In this case, it calls the method from class B, then C, and finally A.

# There are 4 calls instead of 3 because C is called instead of A after B
