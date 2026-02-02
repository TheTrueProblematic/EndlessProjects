
# Woohoo! Welcome to the incredible ride of Catalan number generation! 🎉🚀
# This script will generate a series of Catalan numbers up to a given number, N.
# So buckle up, and let's dive deep into the realms of combinatorial mathematics!

def catalan(n):
    # Hooray for constructing a base case 🏠
    # We start from rock bottom (0) where the Catalan number is 1.
    if n == 0 or n == 1:
        return 1

    # Now, let's summon an array of integers! 
    # It's gonna hold our mighty Catalan numbers. 🛡   
    catalanNums = [0 for _ in range(n + 1)]

    # The first two numbers in our warrior array are 1s. Cool, right? 😎
    catalanNums[0] = 1
    catalanNums[1] = 1

    # Come, let's fill the remaining spots in the array! 👍
    for i in range(2, n + 1):
        catalanNums[i] = 0
        for j in range(i):
            # You see, we keep adding the product of the left and right values to form the next Catalan number.
            # That's the magic formula! ✨😲
            catalanNums[i] += catalanNums[j] * catalanNums[i-j-1]

    # Finally, we return the last value from our array since it will represent the Catalan number for 'n'. 🏁
    # Trust me, it's been a fun journey! 😀
    return catalanNums[n]

# What if our amazing user wants to see a series of these beautiful Catalan numbers? 🤔
# Well, let's not leave them hanging. Here's a function that generates all Catalan numbers up to 'n'!
def generateCatalanNumbersUptoN(n):
    for i in range(n):
        print(catalan(i))

# Here, we are summoning the user to enter a number. 
# It's showtime! Let's display the Catalan numbers upto n! 🥳
n = int(input("Enter the value of N: "))
generateCatalanNumbersUptoN(n)

# Wasn't that fun? Coding is like cracking a magical spell, don't you think? 🧙‍♂️🔮
# Well, that's all for this script. Keep exploring, buddy. Until then, happy coding! 😃
