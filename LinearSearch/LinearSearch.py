
# Hey there, happy coder! This is a fun little script to demonstrate the use of a linear search algorithm.
# It's pretty basic, but it sure does get the job done! 
# Linear search is a simple search algorithm that checks every element in an array until it finds the desired value.

def linear_search(arr, x):
    """
    Function to perform a linear search within a given list.

    Parameters:
    arr(list): List of values.
    x(any type): Value to search for in the list.

    Returns:
    int: Returns index of x in arr if present, else returns -1
    """
  
    # We're looping through the given array here
    for i in range(len(arr)):
  
        # If the current element matches our search value, hooray! Our search ends here.
        if arr[i] == x:
            return i
  
    # Boo, our search value wasn't found in the array. We're returning -1 to indicate this.
    return -1
  
# Try testing it out!
# Define an array of numbers
numbers = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
  
# Let's find the value 110 in the array
search_value = 110

# We're calling our linear search function here. Isn't this exciting?
result = linear_search(numbers, search_value)

if(result!=-1):
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 
