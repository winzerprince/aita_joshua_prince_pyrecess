# Create an E-commerce system that checks input like subtotal, discount, and
# tax to calculate the final price of a product. Include the coupon code for
# discount and tax rate for the calculate
# Use nested conditions to handle different scenarios such as valid/invalid coupon codes
# differnt tax rates based on location , and various dicount levels based on the subtotal amount
#
# Implement login system for the E-commerce platform that checks user credentials and in the
# system, there are 3 types of users: Admin , customers, and Cashiers
# Each user has differnt access levels
#
# E-commerce system
# Author: Aita Joshua Prince (aitajprince100@gmail.com)
#
# Inputs: login details, subtotal, coupon, location
# Outputs: final price
#
# Roles:
# 1. Admin: Can view coupons and tax rates for each location
# 2. Cashier: Can view only coupons
# 3. Customer: Can enter subtotal, coupon and location and get final price
#
# Login:
# Users login using a password and username. All data is stored in memory and doesnt persist across runs

users = {
    "Adam": {"password": "pass1", "role": "Admin"},
    "Reeves": {"password": "pass2", "role": "Cashier"},
    "Jill": {"password": "pass3", "role": "Customer"},
}

# Coupons with their discounts
coupons = {"a111": 0.1, "a222": 0.2, "a333": 0.3}

# Locations with their taxes rates
locations = {
    "Kampala": 0.04,
    "Mbarara": 0.03,
    "Gulu": 0.02,
}

login_attempts = 3
authenticated = False
active_user = ""


# Login using username and password, returns boolean indcating authenticated state
def login(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Weclome")
            return True
        else:
            print(f"Incorrect Password, {login_attempts - 1} attempts remaining")
            return False

    else:
        print(f"Username not found, {login_attempts - 1} attempts remaining")
        return False


while login_attempts > 0:
    username = input("Enter your username:\n")
    password = input("Enter your password:\n")

    authenticated = login(username, password)
    if authenticated:
        active_user = username
        break
    login_attempts -= 1


# Available to Admin and Cachier
def check_coupons():
    print(coupons)


# Available to Admin
def check_tax_rates():
    print(locations)


# Available to Customer
def calculate(subtotal, coupon, location):
    if coupon in coupons:
        if location in locations:
            tax = subtotal * locations[location]
            discount = subtotal * coupons[coupon]

            price = subtotal + tax - discount

            return price


role = users[active_user]["role"]
match role:
    case "Admin":
        print(f"Welcome {active_user}, your role is {role}\n")
        while True:
            num = 0
            print(f"Select a number to perfrom the action")
            print("1. Show coupons")
            print("2. Show tax rates for locations")
            print("3. Exit")
            while True:
                try:
                    num = int(input())
                    break
                except ValueError:
                    print("Please enter a number")
            if num == 1:
                check_coupons()
            elif num == 2:
                check_tax_rates()
            elif num == 3:
                print("Bye")
                break
            else:
                print("Incorrect option, please try again")

    case "Cashier":
        print(f"Welcome {active_user}, your role is {role}\n")
        while True:
            num = 0
            print(f"Select a number to perfrom the action")
            print("1. Show coupons")
            print("2. Exit")
            while True:
                try:
                    num = int(input())
                    break
                except ValueError:
                    print("Please enter a number")
            if num == 1:
                check_coupons()
            elif num == 2:
                print("Bye")
                break
            else:
                print("Incorrect option, please try again")

    case "Customer":
        print(f"Welcome {active_user}, you are a {role}\n")
        while True:
            num = 0
            print(f"Select a number to perfrom the action")
            print("1. Get price")
            print("2. Exit")
            while True:
                try:
                    num = int(input())
                    break
                except ValueError:
                    print("Please enter a number")
            if num == 1:
                subtotal = int(input("Enter the subtotal\n"))
                coupon = input("Enter the coupon code\n")
                location = input("Enter location\n")
                price = calculate(subtotal, coupon, location)
                print(f"The price is {price}\n")
            elif num == 2:
                print("Bye")
                break
            else:
                print("Incorrect option, please try again")
