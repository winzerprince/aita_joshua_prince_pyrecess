# Bill Split Program
# Author: Aita Joshua Prince (aitajprince100@gmail.com)
# Inputs:total bill, tip percentage, number of people
# Outputs: tip amount, bill+tip, bill-per-person

# Declare variables
# Inputs
total_bill = 0.0
tip_percentage = ""
num_of_people = 0

# Outputs
tip_amount = 0
tipped_bill = 0
bill_per_person = 0

print("====================")
print("BILL SPLITTER v0.0.1")
print("====================\n")

# Input gathering in while loops with input validation
while True:
    total_bill = input("Enter the total bill?\n")
    try:
        total_bill = float(total_bill)
        break
    except ValueError:
        print("Invalid input, please try again")


while True:
    # User chooses available options or enters custom value
    print("Choose one of the following tip percentages by entering a, b, c or d")
    print("a) 10%")
    print("b) 15%")
    print("c) 20%")
    print("d) Custom")
    choice = input("")

    match choice:
        case "a":
            tip_percentage = "10"
        case "b":
            tip_percentage = "15"
        case "c":
            tip_percentage = "20"
        case "d":
            tip_percentage = input("Enter a the tip percentage(e.g 10%)?\n")

    # Sanitize input: Remove % if it was added by user
    if tip_percentage.endswith("%"):
        tip_percentage = tip_percentage.rstrip("%").strip()
    try:
        tip_percentage = float(tip_percentage)
        break
    except ValueError:
        print("Invalid input, please try again")


while True:
    num_of_people = input("Enter the number of people sharing the bill\n")
    try:
        num_of_people = int(num_of_people)
        break
    except ValueError:
        print("Invalid input, please try again")


# Calculate output Values
tip_amount = (total_bill * tip_percentage) / 100
tipped_bill = total_bill + tip_amount
bill_per_person = tipped_bill / num_of_people

# Print the Output values
print("\n\n")
print(f"Total bill with tip:        UGX {tipped_bill}\n")
print(f"Tip amount:                 UGX {tip_amount}\n")
print(f"Bill-per-person:            UGX {bill_per_person}\n")
