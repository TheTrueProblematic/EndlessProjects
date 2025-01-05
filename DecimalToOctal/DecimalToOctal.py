# Alright folks, buckle up cos here we go!
# This handy-dandy little Python program is known as the DecimalToOctal converter!
# That's right! This piece of code art can take any decimal number you throw its way.
# And what does it do, you ask? Convert it to its octal equivalent, of course! Who knew it could be this easy!! 

def decimal_to_oct(num):
    """
    Takes a decimal number and converts it into an octal number.
    
    :param num: The decimal number to convert.
    :return: The octal equivalent of the decimal number.
    """
    # Now, let's do some magic here!
    # The built-in Python oct() function does the job. Isn't Python simply wonderful?
    # But watch out! It prefixes the output with "0o" to indicate octal, so we gotta remove that!
    return oct(num)[2:]

if __name__ == "__main__":
    # This little part right here? It's why we call Python considerate.
    # These lines will only run if this file is the main one being executed - if it's imported somewhere else, we'd just be stealing the spotlight!

    # Alright, it's showtime!
    # Let's take an input from the user, making sure it's an integer (we do not want any nasty surprises here!)
    decimal_num = int(input("Enter a decimal number: "))
    
    # Time to call in our octal superhero!
    octal_equiv = decimal_to_oct(num)

    # Drumroll please... and voila! Let's print the result:
    print("The octal equivalent is: ", octal_equiv)

# And there you have it, folks! Your very own Decimal to Octal converter!
# Enjoy converting to your heart's content! Happy coding! 🎉🐍