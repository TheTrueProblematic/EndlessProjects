
# EcologyPredatorPrey.py
# Howdy! Welcome to the wild and wonderful world of ecology simulations!

# This nifty little script will give you a simulation of the classic Lotka-Volterra
# predator-prey model. We're going back to nature here folks! No GUIs, no APIs, no
# internet access, and certainly no frills! Just pure and unadulterated python.
# So sit back, relax, and let's take a stroll through the forest...

# Firstly, it's important to know what we're dealing with
# The Lotka-Volterra equations are a pair of first order, non-linear
# differential equations frequently used to describe the dynamics of
# biological systems in which two species interact, one as a predator
# and the other as prey.

# Here's what the equations look like:
# dx/dt =  alpha*x -   beta*x*y
# dy/dt = delta*x*y - gamma*y

# where:
# x is the number of prey (for example, rabbits)
# y is the number of predators (for example, foxes)
# alpha, beta, delta, gamma are constant parameters

# We're going to need some math magic, so let's import it 
import math

# Our parameters
alpha = 1.0
beta = 0.1
gamma = 1.0
delta = 0.1

# Time step (how fast the simulation runs)
dt = 0.02

# Number of steps to simulate (how long the simulation will run)
steps = 2000

# Initial conditions (start off the simulation with one rabbit and one fox)
x = 1.0
y = 1.0

# Alright, let's dive into our simulation
for t in range(steps):
    dxdt = alpha*x - beta*x*y
    dydt = delta*x*y - gamma*y

    # Apply the changes to our foxes and rabbits
    x = x + dxdt * dt
    y = y + dydt * dt

    # Let's print out how our woodland friends are doing
    print("Time: ", t*dt, " Rabbits: ", x, " Foxes: ", y)

# That's a wrap! Now you're ready to simulate the cycle of life.
# Thanks for joining us and taking a walk through the woods! 

