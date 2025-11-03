
# Hey there, happy pythonista! Welcome to our fun little project of creating a Random Dungeon Generator.

# The theme of the day is 'Random ASCII dungeon layout'. That's right, we're going on a quest to generate a random cool dungeon, entirely in ASCII. Excited? Let's jump right in!

import random

# Here's our room class. Each room's got four walls and a random mystery symbol!
class Room:
    def __init__(self):
        self.symbol = random.choice(['!', '$', '%', '&', '*'])

    def __str__(self):
        return '####\n#{}#\n####\n'.format(self.symbol)

# Time to build our dungeon! It's going to be a list of rooms, so we can easily extend it later.
class Dungeon:
    def __init__(self, size):
        self.rooms = [Room() for _ in range(size)]

    def __str__(self):
        return '\n'.join(str(room) for room in self.rooms)

# Main entry point for our script
def main():
    # First, let's ask the user how big they want their dungeon to be.
    # Don't worry, we'll keep it unitless, because who needs the stress of units in a dungeon?
    size = int(input('How big do you want your dungeon to be? '))
    
    # Now, we make our dungeon with the specified size. Isn't it magical?
    dungeon = Dungeon(size)
    
    # Finally, print out our shiny new dungeon! Our quest is complete!
    print(dungeon)

if __name__ == '__main__':
    main()

# Hope you had as much fun as I did on our ASCII dungeon quest! Until next time, happy coding!



