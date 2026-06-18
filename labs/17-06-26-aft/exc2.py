# Using lambda with sorted

fruits = ["cherry", "banana", "apple", "mango", "orange"]

arranged = sorted(fruits, key=lambda x: len(x))

print(arranged)
