
# Hey there, happy coders! Buckle up because we're going to dive into a wild ride with Bell Numbers today! 
# Bell Numbers are super cool because they count the number of ways you can partition a set, and that's a fun thing to do if you're a set!

# Now, you might be wondering, how do we run this awesome program? Simple! Just run it from your command line and input the N you desire.  
# All right, enough chit-chat. Let's get to coding!

def get_bell_number(n): 
    # Yay, this is where the magic happens!
    # We're defining an N x N list here. Big, I know, but trust me, it's gonna be worth it.
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 

        # Explicitly fill for j = 0 
        bell[i][0] = bell[i-1][i-1] 

        # Fill for remaining values of j 
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1] 

    return bell[n][0] 

# Alright, time to get user input! We want to know how many Bell Numbers they want!
# Remember, no matter what you input, the output will be superbly brilliant.
if __name__ == "__main__":
    n = int(input("Enter the number to generate Bell number sequence up to: "))
    print("The Bell number sequence up to", n, "is: ")
    for i in range(n):
        print(get_bell_number(i))

# And that's the end of our journey! Mission Accomplished! Wasn't that fun?
# Until next time, keep being amazing!

