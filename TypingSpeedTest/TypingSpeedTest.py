
# Hey there, fellow coder! Get ready to have some fun, because we're going to create a typing speed test in Python today. Exciting, huh?
# Remember, we're going to have zero dependencies, which is just another way to say, "we're keeping it simple, baby!"
# Let's get this party started, shall we?

import time

# Let's brainstorm a few sentences for our user to type.
# We could use a random sentence generator, but remember, no internet access allowed!
sentences = ["The quick brown fox jumps over the lazy dog",
             "Pack my box with five dozen liquor jugs",
             "Jackdaws love my big sphinx of quartz",
             "How vexingly quick daft zebras jump",
             "Bright vixens jump, dozy fowl quack"]

# Well, onto the main function of our script, the typing speed test!
def typing_speed_test():

    # First, we'll let the user know what's about to go down.
    print("Get ready for a typing speed test!")
    
    # Now we'll pick a random sentence from our short but sweet collection using the time module
    selected_sentence = sentences[int(time.time()) % len(sentences)]

    # Let's present the challenge to the user.
    print("\Type the following sentence: " + selected_sentence)

    # To calculate the typing speed, we need to start the timer
    start_time = time.time()

    # Get user input
    user_input = input()

    # Stop the timer immediately after user has finished typing.
    end_time = time.time()

    # Now, we'll just take care of some simple error handling. 
    # We wouldn't want to calculate typing speed if the user types nothing, would we? 
    if user_input:
        elapsed_time = end_time - start_time  # total time taken in typing
        words_per_minute = len(user_input.split()) / elapsed_time * 60  # calculate words per minute

        # Now, let's give the user some feedback! 
        print("Your typing speed: %.2f words per minute" % words_per_minute)
        
        # We will also let the user know if he typed the sentence correctly
        if user_input == selected_sentence:
            print("And you typed the sentence correctly. Good job!")
        else:
            print("Oops! You made a mistake while typing.")
    else:
        print("You didn't type anything. Try again!")

    # Aaaand that's a wrap, everyone! A simple python script for a typing speed test, sans dependencies. Cheers!

# Whoa wait, don't forget to call the main function buddy.
if __name__ == "__main__":
    typing_speed_test()

