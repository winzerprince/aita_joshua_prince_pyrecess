# Assignment
# Student Record Management System
#
# Develop a menu-driven Python application that demonstrates all concepts covered in this lesson.
#
# The system should:
#
#     Store student records in a CSV file.
#
#     Save additional student details (e.g., address, contact, program) in a JSON file.
#
#     Allow users to: Add a new student. View all students. Search for a student by registration number. Update student details. Delete a student record.
#
#     Handle all possible errors using try, except, finally, and at least one custom exception.
#
#     Log all user actions and system errors to a log file (student_system.log).
#
#     Include clear comments throughout the code, user-friendly prompts, and appropriate input validation.
#
# Submission Requirements
#
#     Python source code (student_management.py)
#
#     Sample students.csv
#
#     Sample students.json
#
#     Generated student_system.log
#
#     A short report (1–2 pages) explaining the program design, key functions, exception handling strategy, and testing results.

import csv
import json
import logging
from pathlib import Path


CSV_FIELDS = ["RegistrationNo", "Name", "Gender", "Age", "Course", "Score"]
JSON_FIELDS = ["Address", "Contact", "Program"]


class StudentRecordError(Exception):
    """Base exception for student record problems."""


class StudentNotFoundError(StudentRecordError):
    """Raised when a registration number cannot be found."""


class DuplicateStudentError(StudentRecordError):
    """Raised when trying to add a student that already exists."""


class StudentManager:
    def __init__(self, csv_f, json_f, log_f):
        self.csv_f = Path(csv_f)
        self.json_f = Path(json_f)
        self.log_f = Path(log_f)

        logging.basicConfig(
            filename=self.log_f,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True,
        )
        self.logger = logging.getLogger("student_management")

    def _ensure_csv_exists(self):
        if not self.csv_f.exists():
            with self.csv_f.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
                writer.writeheader()

    def _load_csv_records(self):
        self._ensure_csv_exists()
        with self.csv_f.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def _save_csv_records(self, records):
        with self.csv_f.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(records)

    def _load_json_records(self):
        if not self.json_f.exists() or self.json_f.stat().st_size == 0:
            return {}

        with self.json_f.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            records = {}
            for item in data:
                reg_no = item.get("RegistrationNo")
                if reg_no:
                    records[reg_no] = {
                        key: value
                        for key, value in item.items()
                        if key != "RegistrationNo"
                    }
            return records

        return data

    def _save_json_records(self, records):
        with self.json_f.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

    def _find_csv_record(self, reg_num):
        records = self._load_csv_records()
        for record in records:
            if record["RegistrationNo"] == reg_num:
                return record
        raise StudentNotFoundError(f"Student {reg_num} was not found.")

    def get_details(self, reg_nums="", search_json=True):
        """Return student records as a list of dictionaries."""

        try:
            records = self._load_csv_records()
            json_records = self._load_json_records() if search_json else {}

            if reg_nums in ("", None):
                selected_records = records
            elif isinstance(reg_nums, (list, tuple, set)):
                selected_records = [
                    record for record in records if record["RegistrationNo"] in reg_nums
                ]
            else:
                selected_records = [
                    record for record in records if record["RegistrationNo"] == reg_nums
                ]

            merged_records = []
            for record in selected_records:
                merged_record = dict(record)
                if search_json:
                    merged_record.update(json_records.get(record["RegistrationNo"], {}))
                merged_records.append(merged_record)

            return merged_records
        except json.JSONDecodeError as exc:
            self.logger.exception("JSON file is invalid")
            raise StudentRecordError("The JSON data file is invalid.") from exc
        except OSError as exc:
            self.logger.exception("Failed to read student data")
            raise StudentRecordError("Unable to read the student data files.") from exc

    def add_student(self, details):
        try:
            for field in CSV_FIELDS:
                if field not in details or str(details[field]).strip() == "":
                    raise StudentRecordError(f"Missing required field: {field}")

            records = self._load_csv_records()
            reg_num = str(details["RegistrationNo"]).strip()
            if any(record["RegistrationNo"] == reg_num for record in records):
                raise DuplicateStudentError(
                    f"Student {reg_num} already exists and cannot be added again."
                )

            csv_record = {field: str(details[field]).strip() for field in CSV_FIELDS}
            records.append(csv_record)
            self._save_csv_records(records)

            json_records = self._load_json_records()
            json_records[reg_num] = {
                field: str(details.get(field, "")).strip() for field in JSON_FIELDS
            }
            self._save_json_records(json_records)

            self.logger.info("Added student %s", reg_num)
            return csv_record
        except StudentRecordError:
            self.logger.exception("Failed to add student")
            raise
        except OSError as exc:
            self.logger.exception("File write failed while adding student")
            raise StudentRecordError("Unable to add the student right now.") from exc

    def update_student(self, reg_num, details):
        try:
            reg_num = str(reg_num).strip()
            records = self._load_csv_records()
            updated = False

            for record in records:
                if record["RegistrationNo"] == reg_num:
                    for field in CSV_FIELDS:
                        if field != "RegistrationNo" and field in details:
                            value = str(details[field]).strip()
                            if value != "":
                                record[field] = value
                    updated = True
                    break

            if not updated:
                raise StudentNotFoundError(f"Student {reg_num} was not found.")

            self._save_csv_records(records)

            json_records = self._load_json_records()
            if reg_num not in json_records:
                json_records[reg_num] = {field: "" for field in JSON_FIELDS}

            for field in JSON_FIELDS:
                if field in details:
                    value = str(details[field]).strip()
                    if value != "":
                        json_records[reg_num][field] = value

            self._save_json_records(json_records)

            self.logger.info("Updated student %s", reg_num)
            return self._find_csv_record(reg_num)
        except StudentRecordError:
            self.logger.exception("Failed to update student")
            raise
        except OSError as exc:
            self.logger.exception("File write failed while updating student")
            raise StudentRecordError("Unable to update the student right now.") from exc

    def delete_student(self, reg_num):
        try:
            reg_num = str(reg_num).strip()
            records = self._load_csv_records()
            remaining_records = [
                record for record in records if record["RegistrationNo"] != reg_num
            ]

            if len(remaining_records) == len(records):
                raise StudentNotFoundError(f"Student {reg_num} was not found.")

            self._save_csv_records(remaining_records)

            json_records = self._load_json_records()
            json_records.pop(reg_num, None)
            self._save_json_records(json_records)

            self.logger.info("Deleted student %s", reg_num)
            return True
        except StudentRecordError:
            self.logger.exception("Failed to delete student")
            raise
        except OSError as exc:
            self.logger.exception("File write failed while deleting student")
            raise StudentRecordError("Unable to delete the student right now.") from exc


def prompt_student_details(include_registration=True):
    details = {}
    if include_registration:
        details["RegistrationNo"] = input("Enter registration number: ").strip()

    details["Name"] = input("Enter student name: ").strip()
    details["Gender"] = input("Enter gender: ").strip()
    details["Age"] = input("Enter age: ").strip()
    details["Course"] = input("Enter course: ").strip()
    details["Score"] = input("Enter score: ").strip()
    details["Address"] = input("Enter address: ").strip()
    details["Contact"] = input("Enter contact number: ").strip()
    details["Program"] = input("Enter program: ").strip()
    return details


def print_students(records):
    if not records:
        print("No student records found.")
        return

    for record in records:
        print("-" * 60)
        for key, value in record.items():
            print(f"{key}: {value}")


def run_menu():
    manager = StudentManager("students.csv", "students.json", "student_system.log")

    while True:
        print("\nStudent Record Management System")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by registration number")
        print("4. Update student details")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        try:
            if choice == "1":
                details = prompt_student_details(include_registration=True)
                manager.add_student(details)
                print("Student added successfully.")
            elif choice == "2":
                print_students(manager.get_details())
            elif choice == "3":
                reg_num = input("Enter registration number to search: ").strip()
                print_students(manager.get_details(reg_num))
            elif choice == "4":
                reg_num = input("Enter registration number to update: ").strip()
                details = prompt_student_details(include_registration=False)
                manager.update_student(reg_num, details)
                print("Student updated successfully.")
            elif choice == "5":
                reg_num = input("Enter registration number to delete: ").strip()
                manager.delete_student(reg_num)
                print("Student deleted successfully.")
            elif choice == "6":
                print("Goodbye.")
                break
            else:
                print("Please choose a valid option from 1 to 6.")
        except StudentRecordError as exc:
            print(f"Error: {exc}")
        except ValueError:
            print("Invalid input. Please enter valid data.")
        finally:
            print("Action completed.")


if __name__ == "__main__":
    run_menu()
