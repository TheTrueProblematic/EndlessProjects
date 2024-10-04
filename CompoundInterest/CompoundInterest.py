
# Hey there! Welcome to our compound interest calculator!
# I guarantee it's more fun than watching paint dry (unless you're really into paint drying).
# So, sit back, relax, and let's crunch some numbers without lifting a finger, shall we?

def calculate_compound_interest(principal, rate, time, frequency):
    """
    This function calculates the compound interest, pure magic!
    :param principal: The initial sum of money placed in the investment
    :param rate: The annual interest rate
    :param time: The number of times that interest is compounded per year
    :param frequency: The time the money is to stay put in the investment
    :return: the compounded amount
    """
    
    # And now... let's perform our magic trick and compute our compound interest.
    compound_amount = principal * (1 + rate / frequency) ** (frequency * time)
    
    return compound_amount

def main():
    # Prompting users for some essential details.
    print("Hello! Ready to see your money grow? Let's get your details.")
    principal = float(input("Enter your principal amount: "))
    rate = float(input("Enter your annual interest rate (like 0.05 for 5%): "))
    time = int(input("Enter the number of years your money will grow: "))
    frequency = int(input("Enter the number of times interest is compounded per year: "))

    # We're calling our magic function to calculate compound interest.
    result = calculate_compound_interest(principal, rate, time, frequency)

    # Print the result here. Watching money grow was never so easy, eh?
    print(f"Your investment will grow to {result} in {time} years.")
      
if __name__ == "__main__":
    main()

# So there you have it - a nifty little tool to calculate compound interest.
# Remember - a penny saved is a penny earned... or in this case, a penny compounded!
# Happy investing!
