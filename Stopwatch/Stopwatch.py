
# Howdy partners! Welcome to this super fun stopwatch timer code. Yeehaw!

import time

class Stopwatch:
    def __init__(self):
        # Ain't nothin' more important than time, right?
        self.start_time = None
        self.stop_time = None

    def start(self):
        # Get this rodeo started! Don't you worry if it's running already.
        if self.start_time is None:
            self.start_time = time.time()
            self.stop_time = None
        else:
            print("Hey partner, the stopwatch is running already. No need to start it again.") 

    def stop(self):
        # Enough horsing around. It's time to stop.
        if self.start_time is not None:
            self.stop_time = time.time()
            self.start_time = None
        else:
            print("Hold your horses! You can't stop what ain't started.")

    def elapsed_time(self):
        # Y'all wanna know how much time you've been spending? Here you go!
        if self.stop_time is None:
            return time.time() - self.start_time
        else:
            return self.stop_time - self.start_time

    def reset(self):
        # Fresh start! It's like sunrise on the prairie.
        self.start_time = None
        self.stop_time = None

if __name__ == "__main__":
    # Time to put this horse in the race!
    sw = Stopwatch()
    sw.start()
    time.sleep(1)  # Wait a jiffy, let's let the stopwatch tick for a sec.
    print("Elapsed time: ", sw.elapsed_time())
    sw.stop()
    print("Time after stop: ", sw.elapsed_time())
    sw.reset()
    print("Time after reset: ", sw.elapsed_time())

