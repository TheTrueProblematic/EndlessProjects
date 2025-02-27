# Here we go! We're starting with a bang, with a totally fresh and new Python script.
# Our mission, should we choose to accept it, is to find the first occurrence of a substring in a string.
# Sounds pretty neat, right? Let's dive right in, shall we!

def find_first_substring_occurrence(main_string, substring):
    
    '''
    This is our sexy little function that does all the hard work.
    It takes two parameters
     - main_string which is the string where we need to find the substring
     - and substring which is, well, the substring we need to find in main_string. 

    We use the find() function from Python's standard library,
    which is super useful for this kind of stuff!
    The find() function returns the lowest index of the substring if found in given string. 
    If it's not found then it returns -1.
    '''
    
    index = main_string.find(substring)
    return index        
                   
    
# Now let's test this out!
# P.S. Don't forget to replace "Your main string" and "Your substring" with your real inputs. Wink wink!
    
if __name__ == '__main__':
    main_string = "Your main string"
    substring = "Your substring"
    index = find_first_substring_occurrence(main_string, substring)
    
    # Wait wait, before we start, let's print a nice little message to show where the substring was found!
    
    if index != -1:
        print(f"Nice! The first occurrence of the substring is at index: {index}")
    else:
        print("Oops! It seems like the substring is not found in the main string. Please try again!")

# Well, that's it folks! Our Python script is ready!
# This was a fun journey, wasn't it? Until next time, happy coding!