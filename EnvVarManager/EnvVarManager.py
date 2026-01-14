
# Welcome, fellow coder, to the secret abode of EnvVarManager -  your joyful, multi-platform sidekick for managing environment variables.
# This funky little remedy: Lists, adds & removes environment variables without any fuss. The magic happens temporarily, so no worries!
# The best part? No muss, no fuss, no dependencies. Like a pure-blood Python royal, it needs nobody else to perform its wizardry.

# Strapping in? Let's go! 🚀

# Commencing by calling our dear Mr. OS module. 
# Remember, this kind soul doesn't ask for extra install, leaving your Python as fresh as a new spring morning!
import os

class EnvVarManager:
    def __init__(self):
        # Alrighty! Let's kick-start by loading up all our current environment variables in a dict.
        self.env_vars = os.environ.copy()
        
    def list_vars(self):
        # Now, let's roll out the red carpet for our variables!
        for key, value in self.env_vars.items():
            print(f"{key}: {value}")

    def add_var(self, key, value):
        # Drumrolls please! Let's give a big welcome to new variables.
        os.environ[key] = value
    
    def remove_var(self, key):
        # Oops! Time for some variables to say goodbye. But remember, it's not you, it's us.
        if key in os.environ:
            os.environ.pop(key)
        else:
            print(f"No such environment variable: {key}")

# Okay, that's our hard-working EnvVarManager clocking off. Good job, mate!

# Now, it's time for the main performance!
def main():
    manager = EnvVarManager()
    print("Original Environment Variables:")
    manager.list_vars()
    
    print("Adding a new env variable TEMP_VAR with value HELLO_WORLD")
    manager.add_var("TEMP_VAR", "HELLO_WORLD")
    print("Current Environment Variables:")
    manager.list_vars()
    
    print("Removing TEMP_VAR")
    manager.remove_var("TEMP_VAR")
    print("Current Environment Variables:")
    manager.list_vars()

# Phew! What a journey, you champs! 
# Now let's run the show shall we? Give our main function a mighty shout - main()!

if __name__ == "__main__":
    main()

#End of the script, folks!
# Keep being awesome. See you next time in Pycity! 😎
