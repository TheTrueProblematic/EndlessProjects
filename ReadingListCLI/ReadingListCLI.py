
# Hello there, beautiful person! Welcome to the ReadingListCLI program, our super fun "book club" in Python. Let's jump right in!

class Book:
    # Class describing a book! Ain't that fun?
    def __init__(self, title, status="Not Started"):
        self.title = title
        self.status = status
    # Changing the status of the book, because guess what? People read books! 
    def change_status(self, status):
        self.status = status
        print(f"\nYay! You changed the status of {self.title} to {self.status}")

class ReadingList:
    # And now, a class to manage the reading list. Because we can't just have books scattered everywhere, can we?
    def __init__(self):
        self.books = []
    # Adding a book to our list! More books to read, more fun!
    def add_book(self, title, status):
        new_book = Book(title, status)
        self.books.append(new_book)
        print(f"\nWoot! {new_book.title} has been added to your reading list!")
    # Removing a book. Because sometimes, we finish books or (sadly) we give up on them. 
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"\n{book.title} has been removed from your reading list.")
    # Showing our collection of books. Ta-da!
    def show_books(self):
        print("\nHere's your fantastic Reading List!")
        for book in self.books:
            print(f"{book.title} --> {book.status}")

def main():
    # Main function to interact with this marvelous piece of code!
    print("\nHello to our fun and super cool ReadingListCLI program!")
    RL = ReadingList()
    while True:
        print("\nChoices:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Change the status of a book")
        print("4. Show everyone your cool Reading list")
        print("5. Exit the program")
        choice = int(input("\nEnter the number corresponding to your choice and press Enter: \n"))
        if choice == 1:
            title = input("\nEnter the title of the book to add: \n")
            status = input("\nEnter the status of the book: \n")
            RL.add_book(title, status)
        elif choice == 2:
            title = input("\nEnter the title of the book you want to remove: \n")
            RL.remove_book(title)
        elif choice == 3:
            title = input("\nEnter the title of the book you want to change the status for: \n")
            status = input("\nEnter the new status for the book: \n")
            for book in RL.books:
                if book.title == title:
                    book.change_status(status)
        elif choice == 4:
            RL.show_books()
        elif choice == 5:
            print("\nSee you next time for more reading fun!")
            break
        else:
            print("\nOops, that's not a valid option. Please choose from the list!")

if __name__ == "__main__":
    main()
# And that's it, we've come to an end. But don't be sad, this is still Python we're talking about, 
# so the fun never really stops! Until next time, keep reading and keep coding!

