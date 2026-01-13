
# Hey, Happy coder here! Get ready for a fun ride through our script :D
import time
import os
import sys

# We kick off this awesome journey here! First, we'll get the current time
start_time = time.time()

# Now we'll keep a check periodically to see if the session is still active
while True:
    try:
        time.sleep(1)  # Zzzzz for a second, we don't want to eat up your CPU!

        # Hee hee, let's calculate how long the session has been active
        elapsed_time = time.time() - start_time

        # And because I love making things neat and tidy, let's convert this into hours, minutes, and seconds
        elapsed_hours, rem = divmod(elapsed_time, 3600)
        elapsed_minutes, elapsed_seconds = divmod(rem, 60)

        # And now, the drumroll please... Showtime!
        # Check out your amazing achievement of staying active in the session
        print("\rSession has been active for: {:0>2}:{:0>2}:{:05.2f}".format(int(elapsed_hours),int(elapsed_minutes),elapsed_seconds), end="", flush=True)
                            
    except KeyboardInterrupt:
        # Oops! Looks like someone wants to end the session.
        # No worries, let's wrap it up in a nice way!
        print("\nSession ended. Total active time was: {:0>2}:{:0>2}:{:05.2f}".format(int(elapsed_hours),int(elapsed_minutes),elapsed_seconds), end="\n", flush=True)
        sys.exit(0) # Clean exit

# And that's a wrap, folks! Keep coding, keep shining!
# Because remember, coding is a journey, and we're here for the long haul.
# So enjoy every bit of it. And don't forget: Stay happy, stay curious, and keep exploring!


