
# Hey there, lovely human (or cool bot), I'm delighted to present our fabulous little
# ShoppingList app! This script is as pure as a python can be - no frills, no spills,
# just pure pythonic fun!

# No GUI? No problem! No internet or API? Piece of cake! We are going full-steam old school
# with the command line interface here - all the cool kids are doing it!

# Oh, and by the way, I'm totally platform agnostic. Whether you're a Mac lover, a Windows
# enthusiast or a Linux fan, I've got you covered!

# Let's kick things off, shall we?

shopping_list = []  # This is where we'll store our shopping items

def add_item(item):
    """Add an item to our shopping list."""
    if item not in shopping_list:
        shopping_list.append(item)
        print(f'Added {item} to the shopping list! Joy!')
    else:
        print(f'Oops! {item} is already on the shopping list! Good thing we checked, right?')

def remove_item(item):
    """Remove an item from our shopping list."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'Removed {item} from the shopping list! Gone but remembered.')
    else:
        print(f'Oops! We couldn\'t find {item} on the shopping list! Maybe we didn\'t need it after all.')

def view_list():
    """View all items on our shopping list."""
    if shopping_list:
        print('Here are the items on the shopping list:')
        for item in shopping_list:
            print(f'- {item}')
    else:
        print('Woohoo! Nothing in the shopping list. Time to relax!')

def main():
    """Main program function, where our shopping list magic happens."""
    while True:
        print('\nWelcome to the shopping list app! What would you like to do?')
        print('1. Add an item')
        print('2. Remove an item')
        print('3. View the list')
        print('4. Quit')

        # Get the user's choice
        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            item = input('Enter the item to add: ')
            add_item(item)
        elif choice == '2':
            item = input('Enter the item to remove: ')
            remove_item(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            print('Exiting the app. Happy shopping!')
            break
        else:
            print('Invalid choice! Please enter a number between 1 and 4.')

if __name__ == '__main__':
    main()

# Well, that was fun, wasn't it? Our ShoppingList app can now add, remove, and display items.
# I told you it was going to be a blast! Happy coding (or shopping) and see you next time!
