from phonebook import phonebook
def add_contact():
    name = input("Enter  name: ")
    number = input("Enter the  number: ")
    phonebook[name] = number
    print("Contact added successfully.")
def search_contacts():
    name = input("Enter the name to search: ")
    if name in phonebook:
        print("Phone number",phonebook[name])

    else:
        print("Contact not found.")
def delete_contact():
    name = input("Enter the name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
def display_contacts():
    if len(phonebook) == 0:
        print("No contacts found.")
    else:
        print("\n Phonebook contacts:")
        for name, number in phonebook.items():
            print(name,":",number)