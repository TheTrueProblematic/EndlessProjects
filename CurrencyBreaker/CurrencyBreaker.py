
# CurrencyBreaker.py
# Howdy! This is a fun little script to break down a number into currency denominations!
# Whether it's bills or coins, we've got you covered!
# Just give me a number, and I'll show you how many of each denomination you'd need!
# Oh, and remember: no decimals, please!

# First things first, let's define our denominations for both bills and coins
bills = [100, 50, 20, 10, 5, 1]
coins = [0.25, 0.1, 0.05, 0.01]

def currency_breaker(amount):
    """
    Our main function that accepts a total amount and breaks it down into different denominations!
    """
    # A dict to store our results
    breakdown = {}

    # Let's first deal with the bills for whole numbers
    for bill in bills:
        # The fun begins! How many of this bill can we get from the amount?
        num_bills, amount = divmod(amount, bill)
        # Keep the stuff that's left over for the next bill
        # Don't worry, amount! We'll find a home for you too!

        # Add our result to breakdown if we have any bills of this denomination
        if num_bills:
            breakdown['$'+str(bill)] = num_bills
    # Now, let's handle change
    for coin in coins:
        num_coins, amount = divmod(amount, coin)
        if num_coins:
            breakdown[str(coin)+ 'cent'] = num_coins

    # Finally, return the breakdown
    return breakdown

# Run our currency breaker for 245.67 dollars, for example
print(currency_breaker(245.67))

# That's all folks, we did it! Now you can get a breakdown of any number, in terms of currency denominations. Enjoy!
# Remember, we're only as good as the input we get - so no decimals in your dough, ok?
# This was fun! Catch you on the flip side!
