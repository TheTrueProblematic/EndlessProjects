
# Woohoo! What a beautiful day to write an exceptionally joyous piece of Python code! 

# Okay, let's get serious. Today, we will code a trie, also known as a prefix tree. 
# Tries are like trees but cooler - because they're super efficient for looking up words! 

# We shall start, as any story does, with the beginning, our TrieNode.

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
    
    # We're gonna be nice and let our TrieNode tell us if it has a particular child.
    def has_child(self, char: str):
        for child in self.children:
            if child.char == char:
                return True
        return False
    # It's a polite node, isn't it? Now let's move onto our Trie.

class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    # Let's let our Trie know how to add a word.
    def add(self, word: str):
        node = self.root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            # If we didn't find it, add a new child.
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        # Everything finished. Mark it as the end of a word.
        node.word_finished = True

    # Our Trie also needs to know how to check if a word exists.
    def search(self, word: str):
        node = self.root
        for char in word:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            # Return False anyway when not found in child.
            if char_not_found:
                return False
        # Well, we are here means, the Prefix exists
        return node.word_finished

# There you have it! A simple, elegant, no dependency, no frills Trie.
# All from our imagination and the magic of Python.

# Now go and unleash this Trie-tanic force upon your words!
