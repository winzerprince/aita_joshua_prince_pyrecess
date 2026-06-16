# Create a menu driven (GUI), calculator using fucntion for addition, subtraction, multiplication, and division
#


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


# Helper to prompt user for values and print results
def prompt_user(func):
    a = float(input("Enter the 1st number: "))
    b = float(input("Enter the 2nd number: "))

    print("\n=======================")
    if func == mult:
        print(f"{a} x {b} = {mult(a, b)}")
    if func == add:
        print(f"{a} + {b} = {add(a, b)}")
    if func == sub:
        print(f"{a} - {b} = {sub(a, b)}")
    if func == div:
        print(f"{a} / {b} = {div(a, b)}")

    print("=======================")


while True:
    print("=======================")
    print("     KALIKULETA")
    print("=======================")
    operation = input(
        "Choose an operation\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"
    )
    if operation == "1":
        prompt_user(add)
    elif operation == "2":
        prompt_user(sub)
    elif operation == "3":
        prompt_user(mult)
    elif operation == "4":
        prompt_user(div)
