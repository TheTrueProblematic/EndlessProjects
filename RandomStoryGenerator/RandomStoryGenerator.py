
# Hey there, welcome to our fantastic RandomStoryGenerator script! 
# This script is designed to spark creativity by generating a random, short story using a template.

# First things first, we need to import our only dependency - the random module!
# Luckily, it comes pre-installed with Python, so no installation needed (How cool is that?!).
import random

# Now, let's define some templates for the story.
# Each template is a list where each item is a part of the story that gets randomly picked.
# Let's make three templates for the protagonist, the event, and the result.
# More importantly, let's have some fun while doing it!

protagonists = [
    'A curious rabbit',
    'A brave knight',
    'An intelligent orc',
    'An adventurous kid',
    'A cat with nine lives',
]

events = [
    'found a magic stone',
    'bumped into a talking tree',
    'discovered a secret tunnel',
    'met a mythical creature',
    'found a treasure map',
]

results = [
    'and made a lot of friends',
    'but lost it and had a wild adventure',
    'and saved the village',
    'and went on to become a hero',
    'and lived happily ever after',
]


# Here comes the fun part!
# Let's put our story together by randomly picking one part from each template.

def random_story():
    protagonist = random.choice(protagonists)
    event = random.choice(events)
    result = random.choice(results)

    # Let's use string formatting to put together our story.
    story = '{} {} {}.'.format(protagonist, event, result)

    # TADA! We have a random story! Let's print it out.
    print(story)


# Let's make sure our code can be called from the command line
if __name__ == "__main__":
    random_story()
  
# And there you have it, a snazzy little story generator!
# I hope you had as much fun using it as I did writing it. Until next time, keep coding!

