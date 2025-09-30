# Hey there! This is your friendly neighborhood Python program. We're going to have a great time backing up your files into a nifty zip archive!

# Let's start off by importing what we need. No worries, these are all built-in, so no need for any pesky installations!
import os
import zipfile
from datetime import datetime

# Here, let's set the format for our timestamp. Yep, we're keeping it nice and simple!
TIME_FORMAT = '%Y%m%d%H%M%S'

# And here's our main function! Aren't we excited?
def backup_files(*files):
    # This is where the magic happens, folks! First, let's get our timestamp!
    timestamp = datetime.now().strftime(TIME_FORMAT)

    # Now we're getting to the good stuff. Let's stuff all those files into our zip!
    with zipfile.ZipFile(f'backup_{timestamp}.zip', 'w') as backup:
        # And now we're zipping each file, one by one, like a well-oiled machine!
        for file in files:

            # Let's make sure our file actually exists before we try and zip it,
            # or we're going to have a bad time.
            if os.path.exists(file):
                backup.write(file)

            # And if the file doesn't exist? Well, let's not let the user in the dark.
            else:
                print(f"Sorry, could not find the file '{file}'! It will not be included in the backup.")

    # And that's it! Our files are all zipped up and ready to be stored away!
    print(f"Backup archive 'backup_{timestamp}.zip' has been created.")

# And let's not forget to call our function so it actually runs!
if __name__ == "__main__":
    backup_files('file_to_backup1.txt', 'file_to_backup2.txt', 'file_to_backup3.txt')
    