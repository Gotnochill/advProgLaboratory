# Implement a phone directory with add, search, update, and delete options
def print_menu():
    print("\nPhone Directory")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Exit")

directory = {}

while True:
    print_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        directory[name] = phone
        print("Contact added.")
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in directory:
            print(f"{name}: {directory[name]}")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter name to update: ")
        if name in directory:
            phone = input("Enter new phone number: ")
            directory[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in directory:
            del directory[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == '5':
        print("Exiting phone directory.")
        break
    else:
        print("Invalid choice. Please try again.")
