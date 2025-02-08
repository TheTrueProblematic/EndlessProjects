
# Heya, Groovy Coder! Welcome to our Python party! 🎉
# Today, our fun project is to generate some random text using a simple Markov Chain model!
# Remember, no GUIs, no party spoilers like dependencies, or internet access are involved here!
# Let's dive right in!

import random

# Let's start the party by defining our Markov Chain model.
class MarkovChain:
    def __init__(self):
        self.adjacency_map = {}

    # We need to learn from some text data to get this party going!
    def learn(self, data):
        for i in range(len(data) - 1):
            if data[i] not in self.adjacency_map:
                self.adjacency_map[data[i]] = [data[i+1]]
            else:
                self.adjacency_map[data[i]].append(data[i+1])

    # Random text generation, make some noise 🎉
    def generate(self, current_state, no_of_transitions=10):
        result = []
        for _ in range(no_of_transitions):
            if current_state not in self.adjacency_map:
                break
            next_state = random.choice(self.adjacency_map[current_state])
            result.append(next_state)
            current_state = next_state
        return " ".join(result)

# Let's get the party started!
if __name__ == "__main__":
    my_chain = MarkovChain()
    my_text = input("Enter some text to teach the Markov Chain: ")  # Injecting some info
    my_chain.learn(my_text.split())  # Machine learning at its weirdest (in a cool way 😎)
    start_word = input("Enter a word to start the generation: ")  # Ready? Set. Go!
    print(my_chain.generate(start_word))  # Voila! You have some groovy text!

# That's all folks! Simple, clean and portable. Just like we love it.
# Happy Coding! 🎉

