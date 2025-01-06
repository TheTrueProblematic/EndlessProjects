
# Hey there fantastic programmers! 😃 Today, we're gonna whip up a nifty little python program that finds
# the difference of two sets. This is basically stuff present in one set but not in the other. 

# And just a heads up, we are keeping this simple - no GUI, no dependencies, and certainly no internet access. 
# The goal is pure, unadulterated, offline Python fun! 🐍 Let's dive in!

# Oh, and by the way, our dazzling tool du jour is Python's built-in set data type. It's basically a collection of
# distinct (read: no duplicates) elements. And it comes with a ton of cool built-in methods,
# like the one we're going to use for set difference!

def find_difference(set1, set2):
    # The .difference() method comes right out of Python's box of set trinkets. 🎁
    # It works its magic by returning a set that contains the elements present in the first
    # set but not in the second set. Yeah, it's a real tough cookie against duplicates. 🍪

    difference = set1.difference(set2)
    return difference

def main():
    # Hah, you thought we're done? Not quite. Here we'll get our sets from the user. 🕺
    print("Hello there, magical user! Prepare to be amazed by the set difference wizard!💫")

    # Now, let's conjure up some Python charm and get our sets from the user. 💫
    set1 = set(input("Enter some elements separated by a space for the first set: ").split())
    set2 = set(input("Now, be a dear and do the same for the second set: ").split())

    # Abracadabra! Let's get the difference of these sets and fascinate our user!
    difference = find_difference(set1, set2)
    print("\nVoila! The difference of these sets is: ", difference)

if __name__ == "__main__":
    # Let's ignite the spark and get this magic show started! 🔥
    main()

# And that's a wrap, folks! Didn't I promise it would be fun? 🎉 Remember, Python makes savvy use of its built-ins,
# like sets and in-built methods. Keep exploring, keep coding, and above all, keep having fun! 🚀

