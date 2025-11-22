
# Welcome to my wonderful "Traffic Light Simulator"!
# Isn't traffic just the bees' knees? It may not be everyone's cup of tea, but it's a part of everyday city life that we couldn't do without. 
# But we CAN simulate it right here, on our very own command line, from the comfort of home! Isn't that swell?

# We're going to be using the built-in time module here because who doesn't love messing with time?
import time

# Here's where the magic happens, when we define our traffic light class...
class TrafficLight:
    # This is the "constructor" for our traffic light... it gets things started, just like the coffee you had this morning!
    def __init__(self):
        self.color = "red"  # Although red isn't anyone's favorite color to see on the road, it's where we're going to start.

    # Now, for every action there is an equal and opposite reaction... so, when our traffic light changes colors, we're going to print out its state!
    def change_light(self):
        if self.color == "red":
            self.color = "green"
        elif self.color == "green":
            self.color = "yellow"
        elif self.color == "yellow":
            self.color = "red"
        print(f"Traffic light is now {self.color}")

    # We're all about safety here, folks, so we're going to make sure our lights cycle in a reasonable amount of time so as not to cause any accidents!
    def cycle_lights(self):
        while True:
            self.change_light()
            time.sleep(1)  # This will pause the program for a second, which gives us that nice light cycle effect!

# Now that we've got our traffic light all revved up and ready to go, all we need to do is kick-start the cycle!
if __name__ == '__main__':
    light = TrafficLight()
    light.cycle_lights()

# Who knew coding could mimic real-life systems so seamlessly? Just watch out for those red lights!! Drive safe folks!
