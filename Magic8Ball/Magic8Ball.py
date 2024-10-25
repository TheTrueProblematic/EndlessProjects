
# Hey there, happy coder! Welcome to the Magic8Ball script.
# Picture this: You've got a yes or no question, and you simply can't decide on an answer.
# Well, why not consult the mystic powers of the Magic 8 Ball?
# Alrighty, enough chit-chat! Let's get down to the wizardry...uh, I mean, coding.

# First off, let's import our random module - our trusted assistant in generating random numbers.
import random

# Alright amigo, we're going to need a few mystical answers from our Magic 8 Ball.
# Let's store these possible answers in a list.
answers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Next up, let's use that random module to generate a number.
# This will be used to pick out one of the possible answers from our list.
number = random.randint(0, len(answers) - 1)

# Finally, let's print out the chosen answer.
print(answers[number])

# Boom! There you have it! A simple, fun, and mystical Magic 8 Ball simulator. Isn't that fun?
# Now keep calm, keep coding, and may the force be with you!
