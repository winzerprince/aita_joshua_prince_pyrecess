# Using lambda with filter

numbers = [2, 3, 10, 14, 17, 20, 30, 35]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)
