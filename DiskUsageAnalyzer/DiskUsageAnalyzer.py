
# Howdy, fellow code explorer! Welcome to the wild west of disk space analysis!
# Today, we are going on an exciting journey to find out where all your disk space has gone and which folders are the culprits. 

import os  # Our trusty toolkit for handling OS operations

def get_folder_size(start_path='.'):
    """A function that'll wrangle all the information for every file it finds"""
    total_size = 0   # Start the size counter at 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # It's the wild west; exceptions can happen at any time!
            # Here we avoid a crash when finding a file that's too wild to handle.
            try:
                total_size += os.path.getsize(fp)
            except OSError:
                pass
    return total_size


def analyze_disk_usage(start_path='.'):
    """The head honcho function that analyses the disk usage"""
    # An empty list to keep track of our discoveries
    folder_sizes = []
    # We start exploring from the root directory
    for dirpath, dirnames, filenames in os.walk(start_path):
        # Get the size of the current folder
        folder_size = get_folder_size(dirpath)
        # Add the folder and its size to our discoveries
        folder_sizes.append({'folder': dirpath, 'size': folder_size})

    # After the expedition, we sort our discoveries from the greatest to the smallest
    folder_sizes.sort(key=lambda x: x['size'], reverse=True)

    # It's time to report our findings!
    for folder_info in folder_sizes:
        print('Folder: ', folder_info['folder'])
        print('Size: ', folder_info['size'], ' bytes')
        print('--------')


if __name__ == "__main__":
    # As a standalone script, we saddle and start our adventure from the current directory
    analyze_disk_usage('./')

# Yeehaw! Thanks for joining on this exciting adventure. Make sure to come back soon, you hear!
# Suffice it to say, this code has been a hootin' and a hollerin' good time to write. Hope you feel the same way running it!

