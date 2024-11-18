
# Hey there, fellow code enthusiast! This is our little fun script called "SubstringFinder". 
# It's a pretty neat tool, it finds the position of a substring within a string. Simple, but oh-so useful!

# Alright, let's start by defining our main function
def substring_finder():
    
    # Now, we need two things from the user - the main string and the substring they're looking for.
    # Let's get those inputs in a very polite manner.
    main_string = input("Hello! Please enter the string that you want to analyze: ")
    sub_string = input("Great! Now, please enter the substring that you're looking for: ")

    # Now for the fun part. Let's start the search!
    # The find() function will do the magic here. It will go through the string trying to find our substring.
    # It returns the index where the substring starts. If the substring is not found, it returns -1.
    position = main_string.find(sub_string)

    # Depending on what find() gives us, we can tell the user if the substring was found or not.
    if position != -1:
        print(f"Voila! We've found your substring '{sub_string}' in the position {position} of your string.")
    else:
        print("Uh-oh! Your substring does not exist in the given string. Better luck next time!")

# And there you have it! A simple, but fun and effective, substring finder! 
# To kickstart our script, we just need to call the function.
substring_finder()

# That's all, folks! Remember: "The best way to predict the future is to invent it". Keep coding, keep inventing!

