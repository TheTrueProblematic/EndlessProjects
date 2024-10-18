
# Hello there, Happy Pythonistas! Let's dive into the world of health informatics together!

# Here we go! This is a fantastically simple, yet incredibly useful script that we can use to calculate our Body Mass Index (BMI)!
# Super Cool, I know! We're going to rock this without any hard-to-understand scientific mumbo jumbo.

# So, without further ado, let's get started!

def calculate_bmi(height, weight):
    # Alright champ, before we start, remember! Height is in meters and weight is in kg! 
    # Because we are cool scientists who love the metric system! 

    # Our BMI formula is weight divided by height squared!
    # It's a simple process of calculation yet so effective in understanding our bodies!
    bmi = weight / (height ** 2)

    # Just like unwrapping a great present, we will return the surprises (I mean results :P) 
    return round(bmi, 2)

if __name__ == '__main__':
    # Time to test this party trick out!

    # Hey, don't be lazy now, enter your height and weight, let's see that BMI!
    # And remember, no lying, the python can see you!
    height = float(input("Enter your height in meters:"))
    weight = float(input("Enter your weight in kgs:"))

    # Let's call our super function and see what it tells us about our health! 
    result = calculate_bmi(height, weight)
    print("Your Body Mass Index is:", result)

    # There we have it! Great job! Our very own DIY BMI calculator! 
    # Next time, let's dig even deeper into health informatics! See you then!

