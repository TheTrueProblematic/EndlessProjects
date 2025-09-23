
# Hi there! I'm your friendly neighborhood DuplicateFileFinder bot and today I'm gonna 
# help you eliminate duplicate files in your selected directory. Yay! Let's get started.
import os
import hashlib
import sys

def find_duplicates(directory):
    # Wow! Look at all these files! Alright, let's dive right in
    # Creating a dictionary to store file hashes. Keys are the hashes while the values are file paths
    hashes = {}

    # Look at me, walking around directories like it's no big deal! Cool, huh?
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)

            # What's in the box?!? No, I'm not Brad Pitt, just hashing the file!
            file_hash = hash_file(file_path)

            if file_hash in hashes:
                # Hey! I've seen this before! Yup, it's a duplicate!
                hashes[file_hash].append(file_path)
            else:
                # Hmm, this one's new. Let's memorize it for later!
                hashes[file_hash] = [file_path]

    # Time to spill the beans. Gonna show you all the duplicates! Brace yourself! 
    for key, values in hashes.items():
        if len(values) > 1:
            print(f'Duplicate Files for Hash {key} are:')
            for value in values:
                print(f'\t{value}')

def hash_file(file_path):
    # Hmm, you might ask what's this block of code. Well, it's just a basic hashlib function!
    try:
        with open(file_path, 'rb') as f:
            contents = f.read()
            return hashlib.md5(contents).hexdigest()

    except Exception:
        # Sorry, couldn't read the file. It's probably a system file or a directory. My bad!
        return None

if __name__ == "__main__":
    # Trust me, I know what I am doing! Just give me a directory path and see the magic!
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        find_duplicates(directory)
    else:
        print("Ouch! Looks like you forgot to tell me which directory to search in!")
        print("Please give me a directory path like this: python duplicate_file_finder.py <directory_path>")

