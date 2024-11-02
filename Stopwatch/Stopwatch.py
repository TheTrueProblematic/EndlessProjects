
# Hello there, coding preneur! Welcome to our lovely Stopwatch script!
# This handy-dandy program is going to mimic a basic stopwatch.
# It is capable of starting, stopping, and resetting (ain't that cool!).
# It's a little digital buddy right in your terminal.
# So sit tight, grab your popcorn and let's dive right in!

import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.running = False

    # Kickoff our stopwatch! Ain't that fun!
    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
        else:
            print("Hey there, Stopwatch is already running!")

    # Like all good things, our stopwatch also needs to pause sometimes.
    def stop(self):
        if self.running:
            self.stop_time = time.time()
            self.running = False
        else:
            print("Oops! Stopwatch is not running.")

    # Time to get to the point, let's calculate lapsed time.
    def elapsed_time(self):
        if self.running:
            return time.time() - self.start_time
        else:
            return self.stop_time - self.start_time

    # Goodbye past, hello future!
    def reset(self):
        self.start_time = self.stop_time = 0
        self.running = False


# Here comes our main function! It will orchestrate our Stopwatch's performance.
def main():
    stopwatch = Stopwatch()
    while True:
        action = input("Enter 'S' to start, 'T' to stop, 'E' to show elapsed time, 'R' to reset, 'Q' to quit: ").upper()
        if action == "S":
            stopwatch.start()
        elif action == "T":
            stopwatch.stop()
        elif action == "E":
            print(f"Elapsed time: {stopwatch.elapsed_time()} seconds.")
        elif action == "R":
            stopwatch.reset()
        elif action == "Q":
            break
        else:
            print("Whoopsie daisy! Couldn't recognize your command. Kindly punch in again.")

# Invoke the main function in python's style!
if __name__ == "__main__":
    main()

# Woah, you've made it till the end. So proud of you! Wasn't it a thrilling ride?
# Now, you can time yourself while you're coding away to glory!!! How cool is that!
# Keep rocking and keep coding! Until next time, bye!

