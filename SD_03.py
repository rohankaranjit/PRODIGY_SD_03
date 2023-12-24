import json



# Function to load contacts from a file
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

# Function to save contacts to a file
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"{name} added to contacts.")

# Function to view all contacts
def view_contacts(contacts):
    if contacts:
        print("Contacts:")
        for name, contact in contacts.items():
            print(f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts available.")

# Function to edit a contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print(f"Editing {name}:")

        phone = input("Enter new phone number (press Enter to keep existing): ")
        email = input("Enter new email address (press Enter to keep existing): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        save_contacts(contacts)
        print(f"{name}'s contact information updated.")
    else:
        print("Contact not found.")


