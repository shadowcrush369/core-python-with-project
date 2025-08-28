import json
import os

contacts = []

# Load contacts from file (only if it exists)
def load_contacts():
    global contacts
    if os.path.exists("contacts.json"):
        with open("contacts.json","r") as f:
            contacts = json.load(f)

    else:
        contacts = []

# Save contacts to file
def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)       

def add_contact():
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        save_contacts()
        print("Contact added!")

def show_menu():
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Quit")
    print("4. Delete Contact")

def view_contact():
     if not contacts:
          print("No contacts yet")
          return
     for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, phone: {contact['phone']}, Email: {contact['email']}")

def delete_contact():
    view_contact()
    try:
        index = int(input("Enter the contact nunmber ro delete: ")) -1 
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contacts()
            print(f"Deleted dontact: {deleted['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

#Start program
load_contacts()

while True:
    show_menu()
    try:
        choice = int(input("Choose the number between 1 to 4: "))
    except ValueError:
        print("please enter a valid number(1,2,3, or 4).")
        continue

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact()
    elif choice == 3:
        break
    elif choice == 4:
        delete_contact()
    else:
        print("Invalid choice")
