# Student Record Management System Report

## Program Overview

This project is a menu-driven student record management system written in Python. It was designed to meet the assignment requirements by storing the main student profile in a CSV file and storing extra student information in a JSON file. The program supports the five required operations: adding a student, viewing all students, searching by registration number, updating student details, and deleting a record.

The application starts with sample data already loaded in [students.csv](students.csv) and [students.json](students.json), so it can be tested immediately without manual setup. A log file is also generated at [student_system.log](student_system.log) to track user actions and errors.

## Program Design

The main logic is handled by the `StudentManager` class. A class was a good choice here because the assignment needs one central place to manage student data, file paths, and logging. By grouping those responsibilities together, the code stays organized and each operation can reuse the same file-handling logic instead of repeating it in separate functions.

This class acts as the storage layer and contains methods for reading, writing, updating, and deleting records. The CSV file holds the core academic fields: registration number, name, gender, age, course, and score. The JSON file stores the extra profile fields: address, contact, and program. Splitting the data this way matches the assignment instructions and also reflects a practical design choice: CSV is simple and readable for tabular records, while JSON is better for storing nested or extended profile information without forcing every record into the same flat structure.

The `get_details` method reads both files and merges the records so that the user sees one complete student profile instead of two separate data sources. This keeps the interface simple while still satisfying the requirement to use both CSV and JSON files. It also makes searching and viewing more convenient, because the user does not need to inspect two files manually to understand one student.

The menu loop in `run_menu()` provides a user-friendly interface. It displays clear options, asks for the required details, and confirms when an operation succeeds. Invalid menu selections are handled without crashing the program. That approach was chosen because the assignment asks for a menu-driven system, and a loop-based menu is the simplest and most readable way to present the required CRUD operations.

Several helper methods were added to keep the class focused. For example, the CSV and JSON load/save logic is separated into private helper methods so the CRUD methods remain short and easier to test. This reduces duplication and makes the behavior easier to maintain if the file format changes later.

## Exception Handling Strategy

The assignment required error handling with `try`, `except`, `finally`, and at least one custom exception. To meet that requirement, the program uses a small custom exception hierarchy:

- `StudentRecordError` is the base class for all student-management errors.
- `StudentNotFoundError` is raised when a registration number does not exist.
- `DuplicateStudentError` is raised when the user tries to add a student that already exists.

Using custom exceptions gives the program clearer error messages and makes the control flow easier to understand. Instead of treating every problem the same way, the code can distinguish between a missing record, duplicate input, and file or parsing errors. That makes the output more helpful to the user and also makes the code easier to extend.

File reading and writing are wrapped in `try` and `except` blocks so the program can report problems like invalid JSON, missing files, or write failures in a controlled way. The menu loop also uses `finally` so the program prints a completion message after each action, which demonstrates the required cleanup pattern. This ensures the program remains stable even when the user enters bad data or a file operation fails.

## Logging And Validation

Every successful change and every handled failure is recorded in [student_system.log](student_system.log) through Python’s `logging` module. This satisfies the requirement to log user actions and system errors. Logging was used because it is better suited than print statements for storing an audit trail of actions, and it can capture both normal events and exceptions in a consistent format.

Input is also validated so required fields cannot be left blank when adding a student. The implementation checks that registration numbers are unique before inserting a new record. During updates, only the matching student is changed, and during deletion the record is removed from both the CSV and JSON files so the data stays synchronized.

The program also keeps the two data files aligned by using the registration number as the shared key. That choice is important because it gives both files a common identifier and makes lookup, update, and delete operations straightforward.

## Testing Results

The program was tested interactively from the terminal. The following actions were confirmed to work:

1. Viewing all existing records from the sample CSV and JSON files.
2. Searching for a specific student by registration number.
3. Adding a new student record and storing the extra details in JSON.
4. Updating an existing student record.
5. Deleting the added test student.
6. Handling invalid menu input without crashing.

The interactive test session completed successfully and returned to the menu after each operation. This confirmed that the program runs correctly and that the CRUD functions work against the external files as required by the assignment. One of the tests also confirmed that searching for an unknown registration number returns a clear “No student records found” response instead of causing a crash.

## Summary

In short, the project uses a class-based design to keep the data handling clean and reusable, CSV and JSON files to separate core and extended student data, custom exceptions to make error handling more precise, and logging to capture all important actions. The final result is a functional student management system that follows the assignment instructions and can be tested directly from the provided sample files.
