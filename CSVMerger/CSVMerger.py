
# Hello fellow Pythonist! Let's embark on a wonderful journey
# to merge multiple CSV files into a single file! We're gonna have loads of fun!

# We can't embark on any coding journey without our dear friend 'os' and our pal 'csv'.
import os
import csv

def merge_csv_files(filenames, output):
    # First, we'll create a bunch of file handlers for our input CSV files.
    # Think of them like friendly librarians who'll fetch our book (or row of data) whenever we need it! We are opening the files in read mode ('r').
    file_handlers = [open(name, 'r') for name in filenames]
    
    # Let's create a file handler for our destination file--where all of these inputs are going to merge into. 
    # This time, it's in write mode ('w'), because we not only need to fetch books, but also put them back on the shelf in a nicely organized manner!
    out_file = open(output, 'w')

    # Our librarians are great, but they need the help of these csv reader and writer.
    # These guys are like their translators, who can read and write in the dialect of CSV.
    readers = [csv.reader(f) for f in file_handlers]
    writer = csv.writer(out_file) 

    # Now, let's write the headers only once. 
    # We don't want to scare off our readers with repeating headers, do we?
    writer.writerow(next(readers[0]))  

    # After writing the header, let's pour the rest of our data into our destination CSV file.
    # Grab your popcorn, sit back, and watch as our loop comb through the readers to extract and write data into our file!
    for reader in readers:
        for row in reader:
            writer.writerow(row)

    # Phew! It's quite a lot of work, right? But hey, we've done it!
    # Now it's time to close those file handlers. They've worked hard, let's give them a break too!
    for fh in file_handlers:
        fh.close()
    out_file.close()

# This is the starting point of our script. From here on out,
# our code-dragon takes flight!
if __name__ == '__main__':

    # Let's prepare a list of CSV files we want to merge. 
    # You can replace these with the names of your actual files.
    filenames = ['input1.csv', 'input2.csv', 'input3.csv']

    # And let's also prepare the name of our destination file.
    output_file = 'merged.csv'

    # Ok, we're all set! Let's call our merging function
    # and watch the magic happens!
    merge_csv_files(filenames, output_file)

    # And that's it! We've successfully merged multiple CSV files into a single file!
    # Pretty neat, isn't it? Hope you had as much fun as I did!
