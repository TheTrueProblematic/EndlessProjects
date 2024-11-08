# Oh boy! Let's hop right into this fun project.
# We're making a super cool SentenceReverser - A neat little program that flips sentences backwards!
# Strap in, it's gonna be a wild ride. Here we go!

# Importing the sys module, because we need to get some command line arguments
import sys

def reverse_sentence(sentence):
    # The main magic happens here.
    # Yippee! Python makes doing this task easy peasy!
    
    # The split() function makes a list where each word is a separate element
    words = sentence.split()
    
    # then we'll just pull a neat little trick and reverse that list
    words.reverse()
    
    # Then we'll glue it all back together with ' '.join to make it back into one string.
    # And voila! Sentence reversed.
    return ' '.join(words)

def main():
    # Ok, it's show time!
    # Let's grab that sentence argument from the command line.
    sentence = sys.argv[1]
    
    # And we'll feed it to our star function which will cook us a reversed sentence.
    reversed_sentence = reverse_sentence(sentence)
    
    # Last but not least, we print out that beautiful reversed sentence.
    # It's always a joy to see our creation in action.
    print(reversed_sentence)

# This if statement makes sure the code doesn’t run if this file is being imported into another python script. 
# It only runs if it is the main file.
if __name__ == '__main__':
    main()

# And that's it! That's our sentence reverser. Simple and sweet.
# Gosh this was a fun ride! Programming is so much fun when it's like this.
# Well, until the next crazy adventure, this is your happy programmer signing off.
# Keep hacking, folks!