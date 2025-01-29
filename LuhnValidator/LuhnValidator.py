
# Hello there! Welcome to the fun world of the LuhnValidator!
# I'll be your guide. Keep your arms and legs inside at all times. Let's get started!

def validate_card(card_number: str) -> bool:
    '''  
    LuhnValidator - a credit card number validator using the Luhn algorithm.

    This function takes in a card number as a string and returns True if it's a valid credit card number,
    False otherwise.
    '''
    # We'll start by making sure our card number is reversed. Luhn Algorithm starts from the rightmost digit.
    card_number = card_number[::-1]

    # Now, let's split it into two: one for digits in odd places, the other for digits in even places.
    odd_digits = card_number[::2]
    even_digits = card_number[1::2]

    # Let's make sure all digits are actually digits :)
    if not all(digit.isdigit() for digit in card_number):
        return False

    # The Luhn Algorithm encourages us to double every second digit from the right
    doubled_even_digits = [int(digit) * 2 for digit in even_digits]

    # If a digit becomes 10 or more, we subtract 9 from it.
    corrected_digits = [digit if digit < 10 else digit - 9 for digit in doubled_even_digits]

    # We'll take the sum of all the odd digits
    sum_odd_digits = sum(int(digit) for digit in odd_digits)

    # We'll also take the sum of all the corrected digits
    sum_corrected_digits = sum(corrected_digits)

    # Now let's take the total sum of both.
    total_sum = sum_odd_digits + sum_corrected_digits

    # According to the Luhn Algorithm, a valid credit card number will result in a total that ends in 0.
    # So if the remainder when divided by 10 is 0, it's a valid card!
    return total_sum % 10 == 0

# Here's how we call it to validate a card. Just replace the '1234567890123456' with any card number.
# print(validate_card('1234567890123456'))

# Ow~ What a ride! We validated a credit card number with the Luhn Algorithm! Isn't that interesting?
# Thank you for your trust in LuhnValidator. Till next time!
