
# Yay! Let's write some Python code to generate and verify SHA-256 checksum of files. Woohoo!
# Simple and elegant, just like a Python should be! 

# Importing hashlib - Python's own library for secure hashes and message digest algorithms. No external dependencies here, a fresh Python install is more than enough!
import hashlib
import sys

# Function to calculate SHA-256 hash
def calculate_hash(file_path):
    """
    This function calculates the SHA-256 hash of a file.
    @param: file_path (str) : The full path of the file.
    @return: str : The calculated hash value of the file.
    """
    
    # Hiss!! Let's create the hash object for SHA-256.
    hasher = hashlib.sha256()
    
    # Isn't this exciting? We're now going to read the file in binary so it works with all file types!
    with open(file_path, "rb") as fh:
        for chunk in iter(lambda: fh.read(4096), b""):
            hasher.update(chunk)
            
    # There's no escape from the snake's venomous bite (SHA-256 hash) now!
    return hasher.hexdigest()


def main():
    """
    The main function that drives the script.
    """
    
    # Input the file path
    path = input("Enter the complete path of the file: ")
    
    generated_hash = calculate_hash(path)
    print("Generated SHA-256 hash of the file is: ", generated_hash)
    
    print("Do you want to verify this hash against a known value? (yes/no)")
    choice = input().lower()
    
    if choice == "yes":
        known_hash = input("Enter the known hash value: ")
        
        if known_hash == generated_hash:
            print("SHA-256 Checksum verification successful! Your file is safe and sound. :D")
        else:
            print("Uh-oh! SHA-256 Checksum verification failed. Something seems fishy. >_<")
    

# Oh, here is our launchpad! Let's take off!
# We're checking if this script is being run as the main file, and not being imported as a module.
if __name__ == "__main__":
    main()
 
# Fun, wasn't that? We just created a script to calculate and verify SHA-256 hashes of files. With no external dependencies or internet access, and completely CLI-based! Just pure Python magic! Now you can check the integrity of any file at any time with just a simple command. Python at your service! 
 