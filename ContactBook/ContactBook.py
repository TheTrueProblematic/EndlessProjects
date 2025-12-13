
# Hey fellow developers, we are going to have some fun coding a contact book today! Woo-hoo!
# This simple ContactBook program will keep your contacts simple and sweet.. Just like a piece of cake! 

class ContactBook:
    # The ContactBook is initialized with an empty dictionary. 
    def __init__(self):
        self.contacts = {}

    # Let's add some contacts, shall we? This function does just that.
    def add_contact(self, name, phone):

        # Detect any potential duplicates just like a mom detects if you're lying!
        if name in self.contacts:
            print("This contact already exists.")
        else:
            self.contacts[name] = phone
            print(f"Contact added: {name}, {phone}")

    # Going for a search hunt? This function will help you find a contact by name. Easy peasy!
    def search_by_name(self, name):
        try:
            return self.contacts[name]
        except KeyError:
            return "Contact not found."

    # But what if you remembered the number but forgot the name? We got you covered! 
    # This beauty will search the contact by phone number and serve it to you on a silver platter!
    def search_by_phone(self, phone):
        try:
            for name, phoneNumber in self.contacts.items():
                if phoneNumber == phone:
                    return name
            return "Contact not found."
        except KeyError:
            return "Contact not found."

    # Just in case if you have a change of heart and want to delete a contact.. (I mean.. Why?!)
    # This function will do it for you! Bye, bye contact!
    def delete_contact(self, name):
        if name not in self.contacts:
            print("Oops, Can't delete something that doesn't exist!")
        else:
            del self.contacts[name]
            print(f"Contact: {name} is deleted!")

# Alright, now to bring all these pieces together, let's create a command line interface. CLI to the rescue! 
if __name__ == "__main__":
    contact_book = ContactBook()
    while True:
        print("\n1. Add new contact\n2. Search contact by name\n3. Search contact by phone\n4. Delete contact\n5. Quit")
        operation = input("Please choose an operation: ")

        if operation == "1":
            name = input("Please enter the name: ")
            phone = input("Please enter the phone: ")
            contact_book.add_contact(name, phone)
        elif operation == "2":
            name = input("Please enter the name: ")
            print(contact_book.search_by_name(name))
        elif operation == "3":
            phone = input("Please enter the phone: ")
            print(contact_book.search_by_phone(phone))
        elif operation == "4":
            name = input("Please enter the name: ")
            contact_book.delete_contact(name)
        elif operation == "5":
            break
        else:
            print("Incorrect option, please try again!")
            
# And voila! There you have it! A ContactBook, tadaa!      
# Happy coding.. and yes, you're doing AWESOME!
