

"""
Hello there, this is our fun and playful code to estimate the value of π (pi) using the Monto Carlo method.

What a marvellous idea, isn't it?!

Remember back in geometry class, when they told you about the area of a circle? It's π*r^2 right? Good ol' times! 
We're going to use that relation, in the context of a circle enclosed inside a square. 

Why Monte Carlo? Well, that's because we're going to let random points (like throwing a dart blindly) decide whether they fall inside the circle or not.
The more the points we let decide, the closer we tend to get to π. 

Sounds pretty cool, yeah? Sure does. Now sit tight and enjoy the simulation! Let's roll...
"""

# Wow, we don't need a lot of libraries for this. Just the random and math libraries from our good friend python. 
# Such a simple task, yet so much to learn! So let's dive into it...
import random
import math

def estimate_pi(total_random_points):
    """
    This cool function takes in total number of random points for the simulation 
    and estimates the value of pi
    """
    points_inside_circle = 0       
    total_points = 0
    
    # We loop through the range of our total random points
    for _ in range(total_random_points):
        # get our x & y coordinates - random gives us floating numbers in range [0, 1).
        x_rand = random.random() * 2 - 1  # scale it to [-1, 1) 
        y_rand = random.random() * 2 - 1  # scale it to [-1, 1) 

        # distance from origin; remember Pythagoras theorem? 
        origin_dist = x_rand**2 + y_rand**2
        
        # Only consider those points that are inside the circle (distance <= 1)
        if origin_dist <= 1:
            points_inside_circle += 1
            
        total_points += 1 
        
    # Ratio of points circle points to total points times 4 (since circle's area is πr^2 and square's is 4r^2)
    return 4 * points_inside_circle/total_points

# What should be a good number of points? Well, big enough to get a good estimate, 
# but not SO big that it takes the joy out of waiting... 3 million sounds fun!
total_random_points = 3000000 

# Ready to estimate pi? Let's call our function and print it out (with some classic rounding!)
estimated_pi = estimate_pi(total_random_points)
print(f"Estimated Value of Pi, after {total_random_points} iterations, is {round(estimated_pi, 4)}.")

"""
Well, that's all folks! We started with a dart board and ended up with a bit of π, all in a day's work!

I hope you enjoyed using this as much as I did making it. But Mother Computer is calling, and I must roll...
"""

