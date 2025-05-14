import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                name, phone, email, address = line.strip().split('|')
                contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}|{contact['address']}\n")

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    save_contacts(contacts)
    print(" Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print(" No contacts found.")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    keyword = input("🔍 Enter name or phone number to search: ").strip().lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print(f"\n Found Contact:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
            found = True
    if not found:
        print(" No matching contact found.")

def update_contact(contacts):
    name_to_update = input("✏️ Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == name_to_update:
            contact['phone'] = input("New phone number: ").strip()
            contact['email'] = input("New email: ").strip()
            contact['address'] = input("New address: ").strip()
            save_contacts(contacts)
            print(" Contact updated.")
            return
    print("❌ Contact not found.")

def delete_contact(contacts):
    name_to_delete = input("🗑️ Enter the name of the contact to delete: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == name_to_delete:
            contacts.remove(contact)
            save_contacts(contacts)
            print(" Contact deleted.")
            return
    print(" Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid option. Please try again.")

if __name__ == "__main__":
    main()
