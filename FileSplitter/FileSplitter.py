
# -----------------------------------------------------------------------------
# Oh hello there, wonderful person! If you're reading this, it means you're
# about to embark on a journey through my handy-dandy FileSplitter! What a
# day to be alive, am I right?
# -----------------------------------------------------------------------------

import os

def split_file(file_name, chunk_size):
    '''Divide-and-conquer: That's our strategy here. We're gonna take in a file, 
    cut it up into smaller parts, and those parts will be easier to handle.'''

    # Checking file size... Don't want to misjudge how much we can eat!
    file_size = os.path.getsize(file_name)

    # Figuring out how many pieces we'll be cutting our file into
    with open(file_name, 'rb') as f:
        # Each chunk gets a number, like Olympic divers.
        # Better the number, juicier the chunk (Not really!)
        chunk_number = 0
        while True:
            chunk = f.read(chunk_size)
            # Time to break if we're out of file
            if not chunk: 
                break
            chunk_number = chunk_number + 1
            yield chunk
            
        # Now that we're done dissecting let's wrap it up, and go home

if __name__ == "__main__":
    # User! We need to hear your command. What file? How big each chunk?
    file_name = input("Enter the name of the file: ")
    chunk_size = int(input("Enter the size for each chunk (bytes): "))
    
    # We're strapping our boots on, starting the splitting process. 
    # See you on the other side, handler!
    for i, chunk in enumerate(split_file(file_name, chunk_size)):
        chunk_name = f'chunk{i}.bin'
        with open(chunk_name, 'wb') as chunk_file:
            chunk_file.write(chunk)

    # All done! The day is saved. Let's ease up, maybe grab a cup of hot cocoa!
    print("File has been successfully split!")

