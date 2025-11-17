
# Oh, hi there! I see you've stumbled upon my little corner of the python universe. 🌌
# Welcome! I'm designed to produce a random string of emojis, just to add a sprinkle of spice to your day. 🌶️

# And you know what the best part is? I can operate entirely offline, too. Ain't that cool? 🐧
# Using me is easy peasy, lemon squeezy! Just execute this script from the command line, and voila! Emoji galore! 🍋🎉

# Let's get this party started!

import random  # You can't have a party without a bit of randomness! 🥳

# Say hello to our shiny guests: the emoji! 🎭
emojis = (
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", 
    "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", 
    "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", 
    "🧐", "🤓", "😎", "🤩", "🥳", "😏", "😒", "😞", 
    "😔", "😟", "😕", "🙁", "😣", "😖", "😫", "😩", 
    "🥺", "😢", "😭", "😤", "😠", "😡", "🤬", "🤯",
)

def make_emoji_string(length: int) -> str:
    # Oh! This is the center stage! 🎪
    # Here, we use Python magic ✨ to string together a sequence of random emojis from the list above.
    # How many emojis we hear you ask? Well, that's entirely up to you!
    return "".join(random.choice(emojis) for _ in range(length))

if __name__ == "__main__":
    # Setup is done, let's roll the drums and hit the lights! 🥁🔆
    # Feel free to modify this number to get the number of emojis you want. 🎰
    result = make_emoji_string(10)
    print(result)  # There we go, random emojis, fresh from the oven! 🍪👩‍🍳

# That's it! You've just run a tiny part of the python universe. Feel proud! 🚀🎖️

