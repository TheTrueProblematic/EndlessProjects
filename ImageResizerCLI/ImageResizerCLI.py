
"""
    ImageResizerCLI.py
    
    Ahoy there! Welcome to the sea of coding where we'll navigate through the awesome waves of Python.
    What's our quest for today, you ask? 
    Captain, we're undertaking an exciting adventure to resize a ton of images all at once.  
    Grab your compass because we're setting sail with Python's PIL library - our faithful first mate in this endeavor!
"""

# Importing our treasure chest of handy tool:
import os
import sys
from PIL import Image

def resize_image(image_path, output_folder, size):
    """
    This function takes in an image path, output folder and size.
    It opens the image, resizes it and then saves it to the output folder.
    """
    # Time to unlock the treasure chest - our image!
    img = Image.open(image_path)
    
    # Let's resize our gem using the specified size
    img_resized = img.resize((size, size))
    
    # We'll get the original file name (aka the treasure map) to use it for our shiny new scaled down artifact:
    base_name = os.path.basename(image_path)

    # Now, let's bury our treasure in the designated output folder:
    img_resized.save(os.path.join(output_folder, base_name))

    # Whoop-de-doo! We did it, we're done here, Captain!

def main():
    """
    Our CLI is going to need to accept a folder of images to target, 
    an output folder where we can store our resized treasures,
    and the dimensions to resize our images to.
    """
    # Getting the input directory and new size from command line.
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    size = int(sys.argv[3])

    # If our destination to bury treasure doesn't exist, we'll dig up a new one!
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # We're going to scan our initial treasure chest (directory).
    # For each image we find, we'll resize it and save it in our destination chest 
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Resize and save image
            resize_image(os.path.join(input_folder, filename), output_folder, size)

    print(f"All images have been resized and put in {output_folder}")
            
"""
    And that's the end of our swashbuckling adventure, matey! We've resized a bunch of images.
    Hope to do another coding voyage with ye soon. Until then, smooth sailing, lads and lasses!
"""

# Initializing our main function:        
if __name__ == "__main__":
    main()
