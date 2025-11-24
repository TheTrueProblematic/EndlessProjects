
# Howdy partner! 🤠 This here's the EpidemicModel python script.
# Our aim is to mosey on down the trail of disease simulation using our trusty steed, the SIR model.
# So strap in, keep your hands and legs inside the ride at all times, and let's giddy up!

# But hold your horses! 🐴 We're gonna do this without any extra python packages, 
# no GUI, no internet access, and this script will work on any OS where python does. 
# We're coding this python file like cowboys – with nothing but our bare hands and raw python! 

# So, let's draw! 🤠 🔫

# First, we'll define our model parameters. We're using the SIR model, 
# which stands for Susceptible, Infected, and Recovered, the three states folks can be in regarding the disease.

# Total population, N.
N = 1000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.2, 1./10 

# Now, let's get down to the nitty gritty. We're gonna define the SIR model. 🤓
def deriv(state, t, N, beta, gamma):
    S, I, R = state
    # Change in S population over time
    dSdt = -beta * S * I / N
    # Change in I population over time
    dIdt = beta * S * I / N - gamma * I
    # Change in R population over time
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# And now for some python magic! 🧙‍♂️ We're going to use the inbuilt ODE solver of python, odeint.
# We don't need no packages to do our dirty work, we're using built-in python, and that's it! 

from scipy.integrate import odeint

# Initial conditions vector
y0 = S0, I0, R0
# Time grid in days
t = range(0, 160)
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))

# Time to unpack the results, partners! Our journey is about to end! 😥
S, I, R = ret.T 

# Let's print out our simulation results! Ain't technology grand? 😊
print("S:", S)
print("I:", I)
print("R:", R)

# And that's it, our journey is over! 🎉 We've simulated the spread of disease using the SIR model, 
# and all we needed was python, our wits, and a little bit of cowboy spirit! 🤠
# Talk about a hoedown throwdown! 

# Hope you've enjoyed this as much as I did!
# See ya on the trail, partner! 🍻

