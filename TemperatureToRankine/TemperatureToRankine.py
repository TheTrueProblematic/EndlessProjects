
# Hello there! I'm a joyful, cheerful Python script called 'TemperatureToRankine'. 😊
# My mission is to convert Celsius or Fahrenheit temperatures into Rankine. 
# I'm super easy to use and I don't rely on anything but my own code and your input.

# It's very nice meeting you, dear future-user. Here's how to get the most out of me! 

# Let's start with making sure we can interact with the user
import sys

# Next, let's define some happy little functions that will do the conversions. 🌈

def celsius_to_rankine(temp_celsius):
    # Rankine to Celsius conversion: multiply by 9/5 and then add 491.67
    return (temp_celsius * 9/5) + 491.67

def fahrenheit_to_rankine(temp_fahrenheit):
    # Farenheit to Rankine conversion: Just add 459.67
    return temp_fahrenheit + 459.67

# Now, let's prompt the user for their input in our main function

def main():
    # Ask the user if they want to convert from Celsius or Fahrenheit.
    # We'll keep things simple and assume the user won't input anything weird.
    # That seems like a good approach, right? 😁
    scale = input("Hello! Please enter 'C' for Celsius or 'F' for Fahrenheit: ").upper()
    
    # Now let's get the temperature from our friendly user
    temp = float(input("Sure thing! Now, please enter the temperature you want to convert: "))
    
    # Let's do the conversion based on the user's chosen scale!
    if scale == "C":
        result = celsius_to_rankine(temp)
        print(f"Your temperature in Rankine is : {result} R")
    else:
        result = fahrenheit_to_rankine(temp)
        print(f"Your temperature in Rankine is : {result} R")

# And last but not least, let's start this tech party 🎉🎉 by calling our main function
if __name__ == "__main__":
    main()

