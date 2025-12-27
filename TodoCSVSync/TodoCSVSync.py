
# A big hello to everyone reading this wonderful piece of code! 😊
# This is a cheerful and handy tool called TodoCSVSync.
# It's going to help us sync our command-line to-do items into a local CSV file.
# How fantastic is that?
# And the best part is, it doesn't need any fancy GUI or any external dependencies.
# Just pure, simple Python! Let's dive in!

import csv
import sys
import os

# Here are our global variables, our project's workhorses! 😁
FILE_NAME = 'todos.csv'
TODO_LIST = []

def load_todos():
    # Let's load the existing to-do items from our CSV file. 
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                TODO_LIST.append(row[0])

def add_todo(item):
    # Adding a to-do is as easy as pie! 🥧 
    TODO_LIST.append(item)
    # After adding the item, we also need to save it to our CSV file.
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([item])

def show_todos():
    # Look at all the amazing things you've planned to do! 💪
    for index, todo in enumerate(TODO_LIST, start=1):
        print(f"{index}. {todo}")

def main():
    load_todos() 

    while True:
        print("\nWhat can I help with? You can add a TODO or view all the TODOs.")
        print("Type 'add' to add a TODO and 'show' to list all TODOs. Type 'exit' to quit.")
        command = input("> ")
        
        # All right, let's see what we've got here... 🧐
        if command.lower() == "add":
            print("\nWhat is your new TODO?")
            new_todo = input("> ")
            add_todo(new_todo)

        elif command.lower() == "show":
            print("\nHere are all your TODOs:")
            show_todos()

        elif command.lower() == "exit":
            # Time to bid adieu! 👋
            sys.exit()

# Hey there, Python! Please start our program from here. 🚀
if __name__ == "__main__":
    main()
# Well, that's about it folks! This savvy script will help you manage your to-dos efficiently.
# Have fun coding and have a wonderful day! 😄

