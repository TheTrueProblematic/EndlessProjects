
# Hello there! Welcome to the super fantastic journey of JSON to CSV transformation.
# Put on your magical hat because this script will fulfill all your command-line JSON-to-CSV needs.
# Sit tight and enjoy the ride!

# Let's get some essentials ready
import json
import csv
import sys

def json_to_csv(json_file, csv_file):
    # Yay! Time to open the magical door a.k.a JSON file.
    with open(json_file) as magical_door:
        # Let's take a peek inside
        data = json.load(magical_door)

    # Oh look, we found data keys! Let's keep them safe.
    data_keys = data[0].keys()

    # Moving on to the next exciting part i.e opening the CSV file
    with open(csv_file, 'w', newline='') as another_magical_door:
        # Creating a CSV dict writer. Seems like a serious and responsible thing to do.
        writer = csv.DictWriter(another_magical_door, data_keys)
        
        # Writing those keys we found earlier into csv file
        writer.writeheader()
        
        # Filling up the CSV file with data. The magic is happening!!!
        writer.writerows(data)

# Grabbing JSON and CSV file names from those tricky command line arguments. Clever eh?
json_file = sys.argv[1]
csv_file = sys.argv[2]

# And here we are, at the end of our enchanting journey. It's time to call the magic spell a.k.a function.
json_to_csv(json_file, csv_file)

# Voila! The task is done! Enjoy your new CSV and have a wonderful day. Cast more spells soon!


