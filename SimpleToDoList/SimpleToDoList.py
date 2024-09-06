
# Welcome to SimpleToDoList.py! 
# Let's dive into the world of organizing and making life simpler!
# We are going to build a fun and easy way to manage to-dos right from your command-line. No internet, no dependencies, just pure python.

# Alright, let's bring in the magic of python's built-in functionalities!
import sys

# Here's our to-do list. It's just a simple list to start with, but with huge possibilities.
todos = []

def mainMenu():
    # Welcome message to our fun little app!
    print("\nWelcome to SimpleToDoList! The CLI to organize your world!")

    while True:
        # Show them what they can do with our simple, yet powerful app.
        print(
            "\nChoose an action: \n"
            "1 - List tasks \n"
            "2 - Add a task \n"
            "3 - Remove a task \n"
            "0 - Exit app \n"
        )
        
        # Listen to what they've got to say.
        user_choice = input("> ")
        
        if user_choice == "1":
            listTasks()
        elif user_choice == "2":
            addTask()
        elif user_choice == "3":
            removeTask()
        elif user_choice == "0":
            print("Goodbye for now! Don't forget to come back to stay organized!")
            sys.exit()

# Let's show them what's pending in their to-do list.
def listTasks():
    i = 1
    for task in todos:
        print(f"{i}. {task}")
        i += 1

# Let's expand the horizon of their to-do list.
def addTask():
    task = input("Enter the task you want to add: ")
    todos.append(task)
    print("\nTask added!")

# Time to chop down a task off their list.
def removeTask():
    listTasks()
    task_no = int(input("\nEnter the number of the task you want to remove: ")) - 1
    if task_no < len(todos):
        todos.pop(task_no)
        print("\nTask removed!")
    else:
        print("\nOops! No task found. Remember, you're using zero-based indexing!")

# The mystical beginning of our coding journey. In other words, Let's start our little CLI app!
if __name__ == "__main__":
    mainMenu()
