# Sample input for idea1.py
# Contains valid variables, invalid variables, comments, and a docstring.

"""This module is used to test comment handling."""

valid_name = 10
another_valid_name = 20
InvalidName = 30
badName = 40

# This is a comment line
if valid_name < another_valid_name:
    result_value = valid_name + another_valid_name
    print(result_value)

for item in range(2):
    loop_value = item
