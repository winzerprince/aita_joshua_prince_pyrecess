# Contact management system
# # Your Tasks
# Your job is to extend the functionality of the ContactManager class by
# implementing the following requirements. Ensure you do not break the existing features.
#
#  1: Data Validation (20 Points)
# Currently, a user can enter any text for a phone number or email.
# Modify the code to add basic validation:
#
# Phone Validation: In add_contact and update_contact,
# ensure the phone number contains only digits and hyphens (e.g., "+256-701").
# If it contains illegal characters, print an error message and cancel the operation.
#
# Email Validation: Ensure that if an email is provided, it contains an @ symbol and a . (period).
#
#
# Task 2: Advanced Search (25 Points)
# The current Contacts method only filters by name and phone number.
#
# Modify Contactss so that it can also search by email.
#
# Write a helper method or modify the search printout so it displays the search results in a clean,
# user-friendly format rather than just returning a raw Python list of tuples.
#
#
# Task 3: Interactive CLI Menu (35 Points)
# Create an interactive Command Line Interface (CLI) loop inside a function called main().
# When run, the program should present the user with a recurring menu until they choose to exit.
#
# The menu should look similar to this:
#
# === Contact Manager Menu ===CRUD
# 1. Add Contact
# 2. View Contact
# 3. Update Contact
# 4. Delete Contact
# 5. Search Contacts
# 6. List All Contacts
# 7. Exit
# Choose an option (1-7):
#
# Implement proper input handling for each menu item,
# prompting the user for necessary arguments (like name, phone, etc.)
# and passing them to your class methods.
#
# Submission Guidelines:
# 1. Add a single python script to your github link,
# 2. Submit a single Python file named name_contact_assignment.py.

import re
import sys
import termios
import tty


# Put terminal in raw mode and save old terminal settings
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)


def set_raw():
    tty.setraw(fd)


def unset_raw():
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def selector(objs: dict, idx=0):
    """
    This function takes a dictionary of options whose values are and array of function
    and allows the user to select one using the arrow keys
    returns the element in index {idx} of the list of the selected option when the user presses enter.
    """

    set_raw()
    selected = list(objs.keys())[0]
    line = ""
    selector = 0

    # Continuously loop until user presses enter or q to quit
    while True:
        # clear and hide cursor
        sys.stdout.write("\033[2J\033[H\033[?25l")

        # Set cursor to row 1, column 1 and print prompt
        sys.stdout.write("\033[1;1H")
        sys.stdout.write("Choose an option(click up/down arrow key)")

        # List all options
        sys.stdout.write("\033[2;1H")
        for opt in objs.keys():
            if opt == selected:
                line = f"\033[34m > {opt}\033[0m"
            else:
                line = f"   {opt}"

            sys.stdout.write("\r" + line + "\n")
        sys.stdout.flush()

        key = sys.stdin.read(1)
        # q or esc to quit
        if key == "q":
            break
        elif key == "\x1b":  # Arrow keys
            seq = sys.stdin.read(2)
            if seq == "[A":  # Up
                selector = (selector - 1) % len(objs)
            elif seq == "[B":  # Down
                selector = (selector + 1) % len(objs)

            selected = list(objs.keys())[selector]
        elif key in ("\r", "\n"):  # Enter
            return objs[selected][idx]
    unset_raw()


def test_selector():

    def func1():
        print("func1")
        pass

    sample = {
        "opt1": [func1],
        "opt2": [func1, func1],
        "opt3": [func1, func1, func1],
        "opt4": [func1, func1, func1, func1],
        "opt5": [func1, func1, func1, func1, func1],
    }

    value = None
    try:
        value = selector(sample)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print(f"Selected: {value}")


# test_selector()


def search(objs, *keys, prompt="Search contact info: ", formatter=None):
    """
    Takes in a dictionary of objects and allows the user to search by any of the
    specified keys within the object including the object identifier.

    `formatter`, when given, is called as `formatter(key, obj)` to produce the
    one-line label rendered for each match — used to keep search output
    user-friendly instead of dumping the raw dict.
    """

    set_raw()
    query = ""
    match = None
    selector = 0
    selected = None

    while True:
        # clear and hide cursor
        sys.stdout.write("\033[2J\033[H\033[?25l")

        # Set cursor to row 1, column 1 and print prompt
        sys.stdout.write("\033[1;1H")
        sys.stdout.write(prompt + query)

        # List all options
        sys.stdout.write("\033[3;1H")
        matches = []
        for key, obj in objs.items():
            if (
                any(query.lower() in str(obj[k]).lower() for k in keys)
                or query.lower() in key.lower()
            ):
                matches.append((key, obj))

        # Clamp selector if matches shrank under our cursor (e.g. on backspace).
        if matches:
            selector = selector % len(matches)
        else:
            selector = 0

        for i, (key, obj) in enumerate(matches):
            label = formatter(key, obj) if formatter else f"{key}: {obj}"
            if i == selector:
                line = f"\033[34m > {label}\033[0m"
            else:
                line = f"   {label}"

            sys.stdout.write("\r" + line + "\n")
        sys.stdout.flush()

        key = sys.stdin.read(1)
        # ctrl+c to quit
        if key == "\x03":
            break
        elif key == "\x1b":  # Arrow keys
            seq = sys.stdin.read(2)
            if seq == "[A":  # Up
                selector = (selector - 1) % len(matches)
            elif seq == "[B":  # Down
                selector = (selector + 1) % len(matches)

        elif key in ("\r", "\n"):  # Enter
            if matches:
                selected = matches[selector]
                return selected
            else:
                return None
        elif key == "\x7f":  # Backspace
            query = query[:-1]
        else:
            query += key

    unset_raw()


def test_search():

    # Sample structure for contacts object

    contacts = {
        "winzer@gmail.com": {
            "name": "Winzer",
            "phone": "+256-701-000000",
        },
        "adam@gmail.com": {
            "name": "Adam",
            "phone": "+256-701-000001",
        },
        "elain@gmail.com": {
            "name": "Elain",
            "phone": "+256-701-000002",
        },
        "jil@google.onmicrosoft.com": {
            "name": "Jil",
            "phone": "+256-701-000003",
        },
    }

    value = None
    try:
        value = search(contacts, "name", "phone")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print(f"Selected: {value}")


# test_search()


# =============================================================================
# Validation + display helpers
# =============================================================================


# Phone may contain digits, hyphens, plus signs, and spaces only — and must
# contain at least one digit. Matches "+256-701-000000", "0701 000000", etc.;
# rejects "abc", "0701-not-real".
_PHONE_RE = re.compile(r"^[\d\-+ ]+$")


def is_valid_phone(s: str) -> bool:
    return bool(_PHONE_RE.match(s)) and any(c.isdigit() for c in s)


def is_valid_email(s: str) -> bool:
    # Spec: must contain '@' AND '.'. Cheap structural check beyond that —
    # require something on each side of '@' and a '.' in the domain part.
    if "@" not in s or "." not in s:
        return False
    local, _, domain = s.partition("@")
    return bool(local) and "." in domain and bool(domain.replace(".", ""))


def format_contact_line(email: str, obj: dict) -> str:
    """Compact one-liner used in search results + list view headers."""
    return f"{obj.get('name', '-'):<20} {email:<30} {obj.get('phone', '-')}"


def print_contact_block(email: str, obj: dict) -> None:
    """Detailed multi-line view used after a single-record action."""
    print(f"  Name : {obj.get('name', '-')}")
    print(f"  Email: {email}")
    print(f"  Phone: {obj.get('phone', '-')}")


def _prompt(text: str) -> str:
    """input() wrapper that strips and tolerates Ctrl+C / EOF cleanly."""
    try:
        return input(text).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return ""


# =============================================================================
# CRUD operations
# =============================================================================


def add_contact(contacts: dict) -> None:
    """Prompt for a new contact, validate, insert keyed by email."""
    unset_raw()
    print("\n=== Add Contact ===")
    name = _prompt("Name: ")
    if not name:
        print("Name cannot be empty. Cancelled.")
        return

    email = _prompt("Email: ")
    if not is_valid_email(email):
        print("Invalid email — must contain '@' and a '.' in the domain. Cancelled.")
        return
    if email in contacts:
        print(f"A contact with email '{email}' already exists. Cancelled.")
        return

    phone = _prompt("Phone (digits / hyphens / plus / spaces, e.g. +256-701-000000): ")
    if not is_valid_phone(phone):
        print(
            "Invalid phone — only digits, hyphens, '+', and spaces allowed. Cancelled."
        )
        return

    contacts[email] = {"name": name, "phone": phone}
    print(f"\nAdded:")
    print_contact_block(email, contacts[email])


def view_contact(contacts: dict) -> None:
    """Pick a contact via interactive search and print it."""
    if not contacts:
        unset_raw()
        print("\nNo contacts to view.")
        return

    selection = search(
        contacts,
        "name",
        "phone",
        prompt="Search to view: ",
        formatter=format_contact_line,
    )
    unset_raw()
    if selection is None:
        print("\nCancelled.")
        return

    email, obj = selection
    print("\n=== Contact ===")
    print_contact_block(email, obj)


def update_contact(contacts: dict) -> None:
    """Pick a contact and prompt for replacement fields; validate each."""
    if not contacts:
        unset_raw()
        print("\nNo contacts to update.")
        return

    selection = search(
        contacts,
        "name",
        "phone",
        prompt="Search to update: ",
        formatter=format_contact_line,
    )
    unset_raw()
    if selection is None:
        print("\nCancelled.")
        return

    email, obj = selection
    print(
        f"\nUpdating: {obj.get('name', '-')} <{email}>  (leave any field blank to keep)"
    )

    new_name = _prompt("New name: ") or obj["name"]

    new_phone_raw = _prompt("New phone: ")
    if new_phone_raw and not is_valid_phone(new_phone_raw):
        print(
            "Invalid phone — only digits, hyphens, '+', and spaces allowed. Cancelled."
        )
        return
    new_phone = new_phone_raw or obj["phone"]

    new_email_raw = _prompt("New email: ")
    if new_email_raw and not is_valid_email(new_email_raw):
        print("Invalid email — must contain '@' and a '.' in the domain. Cancelled.")
        return
    new_email = new_email_raw or email
    if new_email != email and new_email in contacts:
        print(f"A contact with email '{new_email}' already exists. Cancelled.")
        return

    # Re-key only if the email changed; otherwise update in place.
    if new_email != email:
        del contacts[email]
    contacts[new_email] = {"name": new_name, "phone": new_phone}

    print("\nUpdated:")
    print_contact_block(new_email, contacts[new_email])


def delete_contact(contacts: dict) -> None:
    """Pick a contact and confirm before removing it."""
    if not contacts:
        unset_raw()
        print("\nNo contacts to delete.")
        return

    selection = search(
        contacts,
        "name",
        "phone",
        prompt="Search to delete: ",
        formatter=format_contact_line,
    )
    unset_raw()
    if selection is None:
        print("\nCancelled.")
        return

    email, obj = selection
    confirm = _prompt(f"Delete '{obj.get('name', '-')}' <{email}>? (y/N): ").lower()
    if confirm == "y":
        del contacts[email]
        print("Deleted.")
    else:
        print("Cancelled.")


def search_contacts(contacts: dict) -> None:
    """Interactive search across name / phone / email; print the picked match."""
    if not contacts:
        unset_raw()
        print("\nNo contacts to search.")
        return

    selection = search(
        contacts,
        "name",
        "phone",
        prompt="Search contacts: ",
        formatter=format_contact_line,
    )
    unset_raw()
    if selection is None:
        print("\nNo selection.")
        return

    email, obj = selection
    print("\n=== Match ===")
    print_contact_block(email, obj)


def list_all_contacts(contacts: dict) -> None:
    """Dump every contact in a clean, sorted, user-friendly format."""
    unset_raw()
    print("\n=== All Contacts ===")
    if not contacts:
        print("  (none)")
        return
    # Sort by name (case-insensitive) for stable, readable output.
    print(f"  {'Name':<20} {'Email':<30} Phone")
    print(f"  {'-' * 20} {'-' * 30} {'-' * 18}")
    for email, obj in sorted(
        contacts.items(), key=lambda x: x[1].get("name", "").lower()
    ):
        print("  " + format_contact_line(email, obj))


# =============================================================================
# Entry point — interactive menu loop using the existing arrow-key selector
# =============================================================================


def main() -> None:
    # Mock data loaded fresh on every run, in-memory only.
    contacts: dict = {
        "winzer@gmail.com": {"name": "Winzer", "phone": "+256-701-000000"},
        "adam@gmail.com": {"name": "Adam", "phone": "+256-701-000001"},
        "elain@gmail.com": {"name": "Elain", "phone": "+256-701-000002"},
        "jil@google.onmicrosoft.com": {"name": "Jil", "phone": "+256-701-000003"},
        "samuel.k@example.org": {"name": "Samuel K", "phone": "+1-415-555-0190"},
    }

    # Each menu entry maps to a single-callable list so `selector` (which
    # returns objs[selected][idx], idx=0) hands us the chosen handler.
    # "Exit" maps to None as a sentinel.
    menu = {
        "Add Contact": [add_contact],
        "View Contact": [view_contact],
        "Update Contact": [update_contact],
        "Delete Contact": [delete_contact],
        "Search Contacts": [search_contacts],
        "List All Contacts": [list_all_contacts],
        "Exit": [None],
    }

    try:
        while True:
            chosen = selector(menu)
            # `selector` returns from inside its loop on Enter without
            # restoring the terminal — same convention `test_selector` /
            # `test_search` rely on. Restore explicitly here so the
            # handler's input() prompts behave normally.
            unset_raw()

            # `q` inside selector → None; "Exit" option → None. Same exit path.
            if chosen is None:
                print("\nGoodbye.")
                break

            chosen(contacts)
            _prompt("\nPress Enter to continue... ")
    finally:
        # Always restore the terminal on exit, regardless of how we got here
        # (clean break, exception, Ctrl+C in a handler).
        unset_raw()
        # Show the cursor again — selector / search hid it via "\033[?25l".
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


if __name__ == "__main__":
    main()

