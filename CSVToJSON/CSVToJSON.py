
# Hey there, fun people! Ready to convert some CSV files to JSON format? Well, you're at the right place! Let's start this exciting adventure.

import csv 
import json 

# Fun begins here. We are defining our function to convert a CSV file to JSON format. Smile, it's going to be a smooth ride! 
def convert(csvfile, jsonfile):
    # Opening our CSV file for reading.
    with open(csvfile, 'r') as file:
        # CSV's Dictionary Reader does an amazing job of reading CSV files line by line as ordered dictionary.
        reader = csv.DictReader(file)
        # Python's list comprehension is super handy in dealing with file objects. We convert each row into a dictionary. Great, isn't it?
        data = [row for row in reader]
        
    # And now, let's create our output JSON file. Exciting!
    with open(jsonfile, 'w') as file:
        # JSON's dump function transfers our python list into a JSON string and writes into the file. Voila!
        json.dump(data, file)

if __name__ == "__main__":
    # Here, we are calling our function with our input CSV file name and output JSON file name.
    convert('Input.csv', 'output.json')

# And...We are done! High Five!
# Enjoy exploring your JSON file and catch you on the next Pythonic adventure!


