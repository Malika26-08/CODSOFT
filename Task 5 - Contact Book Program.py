#Contact Book

contacts  = []

def add_contact():
    name = input("Enter a name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter a address: ")
    contact = {"Name": name, "Phone Number": phone_number, "Email": email, "Address": address}
    contacts.append(contact)
    print(" Contact Added!")

def view_contact():
    if len(contacts) == 0:
        print("No Contacts.")
    else:
        print("Your Contacts List")
        for i, contact in enumerate(contacts, start=1):
            print(f"Contact {i}:")
            print(f"Name: {contact['Name']}")
            print(f"Phone Number: {contact['Phone Number']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}")

def search_contact():
    search = input("Enter the name to search: ").lower()
    found = False
    for contact in contacts:
        if contact['Name'].lower() == search:
            print(f"Name: {contact['Name']}")
            print(f"Phone Number: {contact['Phone Number']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}")
            found = True
            break
    if not found:
        print("No Contact Found!")

def update_contact():
    update_name = input("Enter name to update: ").lower()
    for contact in contacts:
        if contact['Name'].lower() == update_name:
            print("\n")
            name = input(f"Name {contact['Name']}:")
            phone_number = input(f"Phone Number {contact['Phone Number']}:")
            email = input(f"Email {contact['Email']}:")
            address = input(f"Address {contact['Address']}:")

            contact['Name'] = name
            contact['Phone Number'] = phone_number
            contact['Email'] = email
            contact['Address'] = address

            print("Contact updated..")
            return

    print("Contact not found!")

def delete_contact():
    if len(contacts) == 0:
        print("No Contact Exists")
    else:
        delete_name = input("Enter the name to delete:").lower()
        for contact in contacts:
            if contact['Name'].lower() == delete_name:
                contacts.remove(contact)
                print("Contact Deleted..")
                return
        print("Contact not found!")

def main():
    while True:
        print("**** MENU ****")
        print("1.Add Contact")
        print("2.View Contact")
        print("3.Search Contact")
        print("4.Update Contact")
        print("5.Delete Contact")
        print("6.Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("Contact to be Added")
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("To Update Contact list")
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exit.")
            break
        else:
            print("Invalid Choice!")

main()
