
# Hello, wonderful world of coding! Today we're going to dive into the fascinating world of text compression, utilizing our friend, the Huffman Coding Tree. Buckle up!

# First things first, we'll need a couple of standard Python libraries. No worries, these come with your standard Python package!
import heapq
import os
from collections import defaultdict

# Alright, let's start creating our own class to act as a node in our Huffman Coding Tree.
class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # we need a way to compare our nodes which are not built-in in Python!
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq

# Now, we're going to create our main class, which will perform the magic of Huffman Coding.
class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    # functions for compression:

    def make_frequency_dict(self, text):
        # Let's create a dictionary where keys are characters and values are their frequency in the given text.
        frequency = defaultdict(int)
        for character in text:
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        # Here we create a priority queue(heapq) where the node with the lowest frequency has the highest priority.
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        # Until we have only one node in our heap, remove two nodes and merge them then push it back to the heap.
        while(len(self.heap)>1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        # If we hit the bottom, it means we found a character. Save its path from the root, the code.
        if(root == None):
            return

        if(root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        # Starting from the root, traverse down to the leaf node(DFS).
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        # Replace each character with its mapped binary string.
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        # Add some padding to the text to be byte-aligned.
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        # Decompose the string into bytes and return the byte array.
        if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return b

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))

        print("Compressed")
        return output_path

