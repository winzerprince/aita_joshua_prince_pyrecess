# What is recursion in functions?
# Recursion in functions is a programming technique where a function calls itself in order to solve a problem.
# It allows for the solution of complex problems by breaking them down into simpler subproblems.
#
# parts of a recursive function
# - Base case: The condition under which the function stops calling itself.
# - Recursive case: The part of the function where it calls itself with modified arguments.
#
# Factorial example:
# In math 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
# In python factorial function can be defined as:
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)
