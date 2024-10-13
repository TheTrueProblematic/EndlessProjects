
# Hey there! welcome to this super fun and cool Python script I like to call "SortingVisualizer". 
# It's like sitting in the front row of a magic show watching an array getting sorted right before your eyes... without the magic wand, of course! 🧙‍♂️

# So, our SortingVisualizer does not require any GUI, dependencies, API or internet connection 
# and can run happily ever after on any platform as long as it has Python slithering around in it :D

# Alright, let's dive in the rabbit hole. Ready? Here we go.

import time # To control the speed of our visualizer

# Let's start with a simple bubble sort.
def bubble_sort(display_list, speed):
    List_Length = len(display_list)
    for i in range(List_Length):
        for j in range(0, List_Length - i - 1):
             
            # Comparing each element with its adjacent
            if display_list[j] > display_list[j + 1] :
                display_list[j], display_list[j + 1] = display_list[j + 1], display_list[j]
                # Time to show off our magic trick
                print(' '.join(list(map(str, display_list))))
                time.sleep(speed)
    
def run_visualizer():
    # Asking user to input numbers separated by a space
    numbers = input("Enter numbers separated by a space: ").split()
    numbers = [int(i) for i in numbers]
    
    # Let's allow the user to set the pace of our show
    speed = float(input("Enter speed of visualizer (in seconds): "))
    
    print("\nAlright, Time to sort these numbers (bubble sort)... hold on tight!\n")
    bubble_sort(numbers, speed)
    print("\nAbracadabra! Your numbers are sorted! Thanks for attending our magic show! 😃")
    
# Our show won't start unless you call the function 😉
run_visualizer()
# Now, watch the magic happen! 🧙‍♂️

