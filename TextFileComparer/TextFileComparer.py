
#Hello World! Welcome To TextFileComparer.py Adventure!
#I'm your trusted Python script ready to be your companion in comparing two text files.
#No GUI, no dependencies, no API or internet, just pure Python! 
#Let's start the adventure, shall we?

#First let's import our torchlight, the sys module, to light our way through!
import sys 

# Function to compare two files 
def compare_files(file1, file2): 
    # Opening files and reading the lines
    with open(file1, 'r') as first_file, open(file2, 'r') as second_file:
        first_file_lines = first_file.readlines()
        second_file_lines = second_file.readlines()
        
    # Let's put on the detective glasses and compare the lines
    for i in range(len(first_file_lines)):
        if first_file_lines[i] != second_file_lines[i]:
            print("Difference found at line", i+1)
            print("In file 1:", first_file_lines[i])
            print("In file 2:", second_file_lines[i])
            print('\n')

#The journey starts here! Time to grab our command-line arguments.
if __name__ == '__main__':
    #We need two text files for this script to run.
    # sys.argv[0] is the script name itself. sys.argv[1] will be the first argument, and sys.argv[2] will be the second.
    if len(sys.argv) != 3:
        print("Oops! You forgot to provide two text files. Try again!")
        sys.exit()

    #The path is clear, let's move forward and start comparing the files!
    compare_files(sys.argv[1], sys.argv[2])
        
#Wow, we made it through the end. High five! 🙏 Remember me whenever you have two text files to compare!

