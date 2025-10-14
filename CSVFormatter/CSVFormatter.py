
# CSVFormatter.py
# Hey, fellow coder! Strap in for some joyous Python scripting. Today, you and I are venturing into the
# whimsical world of formatting and pretty-printing CSV data (hooray!). Now, let's begin our petite programming adventure.

import csv   # No road trip is complete without a map. And in programming, csv is our map. So, let's import it .

def pretty_print_csv(file_path):
    # The function takes one ride buddy along, the 'file_path'. 

    # Open our CSV file using Python's built-in 'open' function.
    with open(file_path, 'r') as csv_file:
        # csv.reader will load our file into memory, ready to be manipulated by our eager-to-please Python code.
        csv_data = list(csv.reader(csv_file))

    # Find the maximum length of data in each column. This will come in handy when we'll print our data.
    max_lengths = [max(len(str(item)) for item in col) for col in zip(*csv_data)]

    # Time to iterate over our data and print it nicely! Look below how Python's f-string functionality 
    # makes it so easy to align our text neatly.
    for row in csv_data:
        print('   '.join(f"{str(item).ljust(length)}" for length, item in zip(max_lengths, row)))
        print('-' * sum(max_lengths) + '-' * 3 * (len(max_lengths) - 1))

# The main driver code begins its journey here. 
if __name__ == "__main__":
    # 'python CSVFormatter.py /path/to/csv' is all you need to type to run this script from the command line.
    import sys
    
    if len(sys.argv) > 1:
        pretty_print_csv(sys.argv[1])  # The first command line argument is the path of the csv file
    else:
        print("Usage: python CSVFormatter.py /path/to/csv")

# And there you have it, a fun, entertaining, and simple way to pretty-print all that bland CSV data. 
# Just remember, Python's simplicity and elegance can make even mundane activities enjoyable!
# Farewell, intrepid code reader. Hope you enjoyed this mini adventure. Stay funky!
