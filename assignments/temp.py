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


for key, obj in contacts.items():
    print(f"{key}, {obj}")

print("Next")

for key in contacts:
    print(key)

print(contacts.items())
