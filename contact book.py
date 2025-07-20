contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Store Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("✅ Contact added successfully!\n")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\n🔍 Contact Found:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

def update_contact():
    print("\n--- Update Contact ---")
    phone = input("Enter the phone number of the contact to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            print("Leave blank to keep current value.")
            contact['name'] = input(f"New Store Name ({contact['name']}): ") or contact['name']
            contact['email'] = input(f"New Email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"New Address ({contact['address']}): ") or contact['address']
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    phone = input("Enter the phone number of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['phone'] == phone:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ").lower()
            if confirm == 'y':
                contacts.pop(i)
                print("✅ Contact deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("❌ Contact not found.")

def menu():
    while True:
        print("""
===== Contact Management System =====
1. Add Contact
2. View Contact List
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
""")
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a number from 1 to 6.")

# Run the menu
menu()
