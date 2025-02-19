
# Hey there, happy coders! We're about to embark on a fun
# little journey, exploring the beauty of geometric progressions.
# We're going to whip up a script that calculates the sum of the first
# N terms of the geometric progression. Hop on and let's get started!

def geometric_sum(a, r, n):
    # Woohoo! We're in the function that does all the magic.
    # We're in the realm of geometric progression, baby!
    # Here's the formula that we're putting to work: a(1 - r^n) / (1 - r)
    # where 'a' is the first term of the progression,
    # 'r' is the common ratio, and 'n' is number of terms
    
    sum = a * (1 - r**n) / (1 - r)
    # Boom! We've done the calculation. The sum of the first N terms!
    return sum

def main():
    # Now we're back to the real world. But we're not here just to chill.
    # We're calling our magical function here.
    # Quick heads up! Be sure to input:
    # a (first term), r (common ratio), n (number of terms)
    a = float(input("Enter the first term, a: "))
    r = float(input("Enter the common ratio, r: "))
    n = int(input("Enter the number of terms, n: "))
    
    # And off we invoke our magic function! 
    sum = geometric_sum(a, r, n)
    
    # And voila! Out comes the sum of the first N terms of the geometric progression, hot and fresh.
    print("The sum of the first", n, "terms of the geometric progression is", sum)

# It's time to set the ball rolling!
if __name__ == "__main__":
    # Let's kickstart our magic journey!
    main()

# Code complete! That was some cool adventure, wasn't it?
# Keep on exploring the wondrous world of coding!
# Happy coding, y'all!
