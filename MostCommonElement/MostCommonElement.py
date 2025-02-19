
# Howdy, fellow Pythonist! Get ready for some fun coding

# Here, we're going to create a Python program that finds the most common element in a list. 
# It's like finding the popular kid in school, but much easier!

# This is an awesome CLI-only operation. No fancy GUIs, no dependencies, no internet access.
# Just pure, wholesome Python on your command line. Ain't coding fun?

def most_common_element(lst):
    """Find the most common element in a list."""
    
    # We're going to use the built-in Python magic to make our lives easier!
    
    # First, let's create a dictionary where the key is an element in the list
    # and the value is the count of that element in the list.
    counts = {i: lst.count(i) for i in lst}
    
    # Now, let's use another built-in function to find the key (element in the list) 
    # that has the greatest value (count in the list). 
    most_common = max(counts, key=counts.get)
    
    # Tada! We found the most common element!
    return most_common

    
def main():
    """Main function to run our most_common_element function."""
    # We're going to test this out with a list of random numbers.
    my_list = [4, 2, 2, 8, 3, 3, 3]
    
    # Call the most_common_element function with the list
    common = most_common_element(my_list)
    
    # And let's print the result in the console!
    print("The most common element is:", common)


# Python's way of telling the program, "Start here!"
# Isn't Python just the best?
if __name__ == "__main__":
    main()

