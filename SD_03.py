
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
# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} deleted from contacts.")
    else:
        print("Contact not found.")
        # Main function to manage contacts
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add a contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()




