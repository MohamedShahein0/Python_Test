contacts = []

import os

file_path = os.path.join(os.path.dirname(__file__), "contacts.txt")

try:
    with open(file_path, 'r') as file:
        for line in file:
            name, phone, email = line.strip().split(',')
            contacts.append({"name": name, "phone": phone, "email": email})
except FileNotFoundError:
    pass

def save_contact():
    with open(file_path, 'w') as file:
        for person in contacts:
            file.write(f"{person['name']},{person['phone']},{person['email']}\n")

while True:
    choice = input('1. Add new contact\n2. View contacts\n3. Search contact\n4. Exit\nChoose:   ')
    if choice == '1':
        while True:
            person = {}
            person['name'] = input('Enter name:   ')
            person['phone'] = input('Enter phone number:   ')
            person['email'] = input('Enter email:   ')
            contacts.append(person)
            save_contact()
            another = input('Do you want to add another person(yes/no):   ').lower()
            if another != 'yes':
                break
        for person in contacts:
            print(f"Name: {person['name']}")
            print(f"Phone: {person['phone']}")
            print(f"Email: {person['email']}")
            print("-----")
    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        for person in contacts:
            print(f"Name: {person['name']}")
            print(f"Phone: {person['phone']}")
            print(f"Email: {person['email']}")
            print("-----")
    elif choice == '3':
        ask_name = input('Enter the persons name:   ')
        found = False
        for contact in contacts:
            if contact['name'].lower() == ask_name.lower():
                print("Phone:", contact['phone'])
                print("Email:", contact['email'])
                found = True
                break
        if not found:
            print("Contact name not found.")
    elif choice == '4':
        save_contact()
        break