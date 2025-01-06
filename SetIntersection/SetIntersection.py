
# Hey there, Happy Coders!
# Get ready to plunge into a cool, minimalistic Set Intersection program! This little beauty is perfect
# when you've got two sets and you desperately need to find what they have in common. Great eh? 
# Fasten your seat belts, we're going multi-platform!

def find_intersect(set1, set2):
    # Oh, Intersection! The maths class memories, right?
    # Python sets make it so easy and fun!
    intersection = set1 & set2

    # There you go, your intersecting elements!
    return intersection


def main():
    # Let's pretend that we're in a universe with two sets. What would they be? Anything you'd like!

    # Set 1: An incredibly fun set of numbers!
    set1 = {1, 2, 3, 4, 5}

    # Set 2: Another outrageously fun set of numbers!
    set2 = {3, 4, 5, 6, 7}

    # Let's call our little function to work its magic!
    print(find_intersect(set1, set2))

# This is the fun part: If the python universe decides this file should be the entry point,
# our mega-awesome main function will kick things off!

if __name__ == "__main__":
    main()
# And that's the end of our fun journey, Happy Coders!
# Hope you'll enjoy finding intersections as much as we enjoyed coding this!
# Keep on coding and have a great day!

