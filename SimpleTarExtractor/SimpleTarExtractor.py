
# Hey there, lovely programmer!
# Welcome to the fun land of automated TAR file extraction with Python.
# Our cheerful little Python script will help you extract files from a .tar archive.
# It's simple, neat, and just a ray of sunshine on a gloomy coding day!

import tarfile  # We need this buddy to handle tar files
import sys  # Oh, and this one to interact with the command line

def extract_tar(file_path, destination):
    """
    Hooray! Let's extract some tar files!

    Parameters:
    file_path (str): The path to the tar file we'd love to extract
    destination (str): The location where we'll put the extracted files 
    """
    try:
        with tarfile.open(file_path) as tar:  # Let's open the tar file
            tar.extractall(path=destination)  # And extract it to our given location
            print(f"Successfully extracted files to {destination}")
    except Exception as e:
        print(f"Oh dear! Something went wrong. Here's the error: {e}")
        sys.exit(1)  # We'll exit with an error status code because things didn't go as planned

if __name__ == "__main__":
    # Check if user gave us the tar file and the extraction location.
    if len(sys.argv) != 3:
        print("Oopsie! You must provide the tar file path and the destination path.")
        sys.exit(1)  # Exit the program because we need those details to continue
        
    tar_file, dest_path = sys.argv[1], sys.argv[2]  # Unpacking the command line arguments
    extract_tar(tar_file, dest_path)  # Let's get this party started!
    
# And that's all folks! Happy extracting, and remember, a rainbow is just a refraction away! 🌈
