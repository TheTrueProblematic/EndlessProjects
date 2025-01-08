"""
Hey there, happy coder! You've stumbled upon a (admittedly very simple) majority-vote system!
Our system gets votes as input and determines the winner based on the majority of votes.
No GUI, no dependencies, and definitely no internet access required.
Just pure, delightful Python! Let's get started, shall we?!
"""

def majority_vote():
    """
    A function to simulate a simple majority based voting system.
    """
    # Initialize an empty dictionary to store the votes
    votes_count = {}

    while True:
        # Prompt for a vote
        vote = input("\nEnter your vote (or 'q' to quit): ")

        # Check if the user wants to quit
        if vote.lower() == 'q':
            break
        # If the vote is already in the dictionary, increment the count, otherwise add it with a count of 1
        if vote in votes_count:
            votes_count[vote] += 1
        else:
            votes_count[vote] = 1

    # We have to determine the winner, very exciting times!
    winner = max(votes_count, key=votes_count.get)

    print(f"\nAnd the winner is... {winner}!")

"""
There you have it, fellow coder! A basic, yet charmingly effective, majority-vote system.
Just remember, every vote counts, even the simulated ones!
Take this code, run it, modify it, and have fun. That's what coding's all about!
"""


# We don't want to forget to actually call our voting function, right? Here's to democracy in action!
if __name__ == "__main__":
    majority_vote()