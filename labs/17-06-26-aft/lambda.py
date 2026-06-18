# Advanced Functions
# What are lambda functions ?
# # Lambda functions are anonymous functions that can have any number of arguments but only one expression.
# syntax: lambda arguments: expression
# key charactersistics of lambda functions:
# 1. They are anonymous functions, meaning they do not have a name.
# 2. They can have any number of arguments, but only one expression.
# 3. They are often used as a quick way to define simple functions for short-term
#
# Binary search algorithm
def binary_search(arr, target, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(arr, 5, 0, len(arr) - 1)

print(f"Target {target} found in array: {result}")
