
# Hey there! Welcome to MarkdownTableGenerator.py! 🚀
# This little piece of code is super handy, it helps you generate a markdown table from user input right from your command line!
# Let's dive right in and start the code-adventure!

# Let's import os (one of Python's standard library)
import os

def generate_table():
    # Hooray, we are in the function that generates our markdown table! 🥳
    # Let's start with an empty table!
    table = "|"

    # Let's ask the user how many columns they want in the table.
    num_columns = int(input("Enter the number of columns you want in the table: "))

    # Now, for every column, we ask the user to name it,
    # and we add it to our table with some markdown format.
    # Also, we add an extra '|---|' for formatting purposes.
    for i in range(num_columns):
        column_name = input(f"Enter name for column {i+1}: ")
        table += f" {column_name} |"
    table += "\n|" + " --- |"*num_columns

    # Now, up next we let the user add the rows they want! 😄
    # They can keep adding as many rows as they like until they're satisfied.
    while True:
        response = input("Do you want to add a row? Y/N: ")
        if response.lower() == "n":
            break
        table += "\n|"
        for i in range(num_columns):
            cell_value = input(f"Enter value for cell {i+1}: ")
            table += f" {cell_value} |"

    # And that's a wrap folks!
    # Finally, we print the table and it's all nicely formatted and shiny!
    print(table)

   
if __name__ == "__main__":
    # And here we go, adventure starts here! 😉
    # We only want to run this function if we run this script directly.
    # That's why we check for __name__ == "__main__"

    print("Hello! Welcome to your friendly MarkdownTableGenerator! Let's create a table🎈\n")
    generate_table()
    
# That's all folks! Hope you have loads of fun generating those markdown tables. 🎉

