# Python Learning Demo Script
# This script demonstrates various Python concepts: File Handling, CSV/JSON processing, Exception Handling, and Logging.

import csv
import json
import logging
import os

# ========================================
# 1. File Handling: Open, Read, Write, Append, Close
# ========================================
print("=== 1. Basic File Handling ===")

# Writing to a file (overwrites if exists)
with open("example.txt", "w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("Line 2: Learning Python file handling.\n")
print("Written to example.txt")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("Content of example.txt:")
    print(content)

# Appending to a file
with open("example.txt", "a") as f:
    f.write("Appended line: This is new content.\n")
print("Appended to example.txt")

# Reading again
with open("example.txt", "r") as f:
    print("Updated content:")
    print(f.read())

print("\n")

# ========================================
# 2. Handling CSV Files
# ========================================
print("=== 2. Handling CSV Files ===")

# Reading CSV
print("Reading students.csv:")
with open("students.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Writing a new CSV
new_students = [
    ["2026/BSCS/006", "Frank Kimani", "Male", 21, "Python Programming", 82],
    ["2026/BSCS/007", "Grace Wanjiku", "Female", 22, "Python Programming", 95],
]

with open("new_students.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["RegistrationNo", "Name", "Gender", "Age", "Course", "Score"])
    writer.writerows(new_students)
print("Written new_students.csv")

# Appending to CSV
with open("new_students.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["2026/BSCS/008", "Hellen Atieno", "Female", 20, "Python Programming", 76]
    )
print("Appended to new_students.csv")

# Reading with DictReader (more convenient)
print("Updated CSV content with DictReader:")
with open("new_students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
print("\n")

# ========================================
# 3. Handling JSON Files
# ========================================
print("=== 3. Handling JSON Files ===")

# Reading JSON
print("Reading students.json:")
with open("students.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(data)

# Writing JSON
new_data = [{"Name": "John", "Age": 30}, {"Name": "Jane", "Age": 25}]

with open("new_students.json", "w") as jsonfile:
    json.dump(new_data, jsonfile, indent=2)
print("Written new_students.json")

# "Appending" to JSON (read-modify-write pattern)
if os.path.exists("new_students.json"):
    with open("new_students.json", "r") as jsonfile:
        existing = json.load(jsonfile)
    existing.append({"Name": "Bob", "Age": 28})
    with open("new_students.json", "w") as jsonfile:
        json.dump(existing, jsonfile, indent=2)
print("Appended to new_students.json")

# Reading updated
with open("new_students.json", "r") as jsonfile:
    print("Updated JSON:")
    print(json.load(jsonfile))
print("\n")

# ========================================
# 4. Debugging and Exception Handling
# ========================================
print("=== 4. Exception Handling ===")


def divide_numbers(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError as e:
        print(f"Error: Division by zero - {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:  # Catch-all
        print(f"Unexpected error: {e}")
    finally:
        print("This always executes - cleanup here.")


# Test cases
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "a")  # Type error example

# Raising custom exceptions
print("\nRaising custom exception example:")


class CustomError(Exception):
    pass


try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(f"Caught custom error: {e}")
print("\n")

# ========================================
# 5. Debugging using Logging Module
# ========================================
print("=== 5. Logging Module ===")

# Configure logging (to file + console)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

logger.debug("This is a debug message - for detailed troubleshooting")
logger.info("This is an info message - general information")
logger.warning("This is a warning message - something might be wrong")
logger.error("This is an error message")
logger.critical("This is a critical message")

# Logging inside exception handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    logger.error(f"Division error occurred: {e}", exc_info=True)

print("Check app.log for logged messages.")
print("\nDemo complete!")
