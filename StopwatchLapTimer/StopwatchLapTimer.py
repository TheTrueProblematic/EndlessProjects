
# Woohoo, Timer fun begins! Let's dive into some cool python coding.
# So, we are creating an exciting Stopwatch program with lap recording functionality using Python.
# And the best part? No GUI, no dependencies. Just pure, simple sweet Python!

# Importing time module for our timer operations
import time

class Stopwatch:
    """
    Our Stopwatch class. Right now, it's empty but soon it would be brimming with timey wimey stuff!
    """
    def __init__(self):
        # Starting with setting all values to None
        self.start_time = None
        self.end_time = None
        self.laps = []

    def start(self):
        """
        Wooosh! And we start the stopwatch!
        """
        self.start_time = time.time()

    def stop(self):
        """
        Stop! Hammer Time!
        """
        self.end_time = time.time()

    def lap(self):
        """
        Time for a lap! Calm down Michael Schumacher, just a Python lap!
        """
        lap_time = time.time() - self.start_time
        self.laps.append(lap_time)
    
    def get_time(self):
        """
        Get time of stopwatch. Who needs Doc Brown's time machine!
        """
        return time.time() - self.start_time

# Let's start the fun! 
stopwatch = Stopwatch()

# Run the stopwatch
stopwatch.start()

# Let's wait and pretend we're having a pizza
time.sleep(1)  # Change this to simulate different time periods

# Took a lap!
stopwatch.lap()

# Another wait, maybe for ice cream now?
time.sleep(2)  # Change this to simulate different time periods

# And another lap!
stopwatch.lap()

# Finally, let's stop the stopwatch.
stopwatch.stop()

# Now let's show our lap times. Ready? Here they come!  
for i, lap in enumerate(stopwatch.laps, start=1):
    print(f'Lap {i}: {lap} seconds')

# And that's it! We've made a cool CLI-based Stopwatch with Python. High five!
