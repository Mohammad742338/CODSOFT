class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        """Add a new contact to the contact book."""
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")

        contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
        self.contacts.append(contact)
        print(f"\nContact '{name}' added successfully!")

    def view_contacts(self):
        """Display all saved contacts."""
        if not self.contacts:
            print("\nNo contacts found!")
            return
        
        print("\nContact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self):
        """Search for a contact by name or phone number."""
        search = input("Enter name or phone number to search: ").lower()
        found_contacts = [c for c in self.contacts if search in c['name'].lower() or search in c['phone']]
        
        if found_contacts:
            for contact in found_contacts:
                print(f"\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
        else:
            print("\nNo contact found!")

    def update_contact(self):
        """Update an existing contact's details."""
        search = input("Enter the name or phone number of the contact to update: ").lower()
        for contact in self.contacts:
            if search in contact['name'].lower() or search in contact['phone']:
                print(f"\nUpdating contact: {contact['name']}")
                contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
                contact['phone'] = input("Enter new phone number (leave blank to keep current): ") or contact['phone']
                contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
                contact['address'] = input("Enter new address (leave blank to keep current): ") or contact['address']
                print(f"\nContact '{contact['name']}' updated successfully!")
                return
        print("\nNo contact found to update!")

    def delete_contact(self):
        """Delete a contact from the contact book."""
        search = input("Enter the name or phone number of the contact to delete: ").lower()
        for i, contact in enumerate(self.contacts):
            if search in contact['name'].lower() or search in contact['phone']:
                confirm = input(f"Are you sure you want to delete '{contact['name']}'? (yes/no): ").lower()
                if confirm == 'yes':
                    self.contacts.pop(i)
                    print(f"\nContact '{contact['name']}' deleted successfully!")
                    return
        print("\nNo contact found to delete!")

    def main_menu(self):
        """Display the main menu for the contact book."""
        while True:
            print("\n--- Contact Book Menu ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid option! Please choose a number between 1 and 6.")

if __name__ == '__main__':
    contact_book = ContactBook()
    contact_book.main_menu()
