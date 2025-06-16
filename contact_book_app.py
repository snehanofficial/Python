# Build a contact manager:
# 	•	Add contact (name, phone, email)
# 	•	Search by name
# 	•	Delete a contact
# 	•	View all contacts

contacts = []

def add_contact(name, phone, email):
    contacts.append({"name": (name.strip()).lower(), "phone": int(phone), "email": email.lower()})
    return print(f"{name} - Contact added successfully.")

def search_contact(search_name):
    for phone, name in contacts.items():
        if name == search_name:
            print(f'''Name: {name}
Phone: {phone}
Email: {email}''')
            return
    print("Contact not found")

def delete_contact(del_name):
        for key, name in contacts.items():
            if name == del_name:
                contacts.remove(name)
                print(f"{del_name} - Contact deleted successfully.")
                return

def view_contacts():
    for i, c in enumerate(contacts, 1):
        print(f"{i}. ", end="")
        for key, value in c.items():
            print(f"{key} : {value}")
        print()

while True:
    print("\n=== Welcome to the Contact Manager ===")
    print("Enter 1 to add a new contact")
    print("Enter 2 to search a contact")
    print("Enter 3 to delete a contact")
    print("Enter 4 to view all contacts")
    # print("Enter 0 to Exit")
    option = int(input("Enter your choice: "))

    if option == 1:
        name, phone, email = input("Enter the name, phone number and email [Separated by a comma(,)]: ").split(",")
        add_contact(name, phone, email)
    
    elif option == 2:
        name = input("Enter the contact name to search: ")
        search_contact(name)
    
    elif option == 3:
        del_name = input("Enter the contact name to delete: ")
        delete_contact(del_name)
    
    elif option == 4:
        view_contacts()
    
    # elif option == 0:
    #     print("Thank you!")
    
    else:
        print("You have entered an invalid response.\nPlease, Try again. ")