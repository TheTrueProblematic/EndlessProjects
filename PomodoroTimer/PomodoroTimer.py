
# -*- coding: utf-8 -*-
"""
Hey there buddy! 
We're about to make a magic happen. Yeap, we're gonna implement our dear, beloved Pomodoro Timer! 
No GUI, no fancy buttons or sliders, just good old Python and console window.
We're gonna have awesome work and break intervals to boost our productivity.
So, let's do it!

Oh, just a reminder - please, never ever run this app while you're driving or baking muffins - 
we wouldn't want those beauties to burn, would we? ;)
"""

"""
Let's start with our imports. 
We're gonna need 'time' module for our timer and 'sys' module to gracefully exit our app when needed.
Don't worry, both modules are built-in so no need to hassle with any installations!
"""
import time
import sys

WORK_TIME = 25 * 60  # Work time in minutes. Tomatoes love a good 25-min workout!
BREAK_TIME = 5 * 60  # Short break time in minutes. Well-deserved 5 mins of rest!

def countdown(time_interval):
    """
    A good old boring countdown function that takes an interval (in seconds) and counts down to 0.
    
    Remember, time flies when you're having fun! Or coding... or whatever you're doing ;)
    """
    while time_interval:
        mins, secs = divmod(time_interval, 60)
        work_or_break = 'Work that tomato now!' if time_interval == WORK_TIME else 'Break time, my friend!'
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'{work_or_break} Remaining - {timer}', end="\r")
        time.sleep(1)
        time_interval -= 1
          
def pomodoro_timer():
    """
    Exactly what it sounds like - Tomato Timer! (Pomodoro is Italian for Tomato, remember?)
    
    So, our first Tomato Timer... There's always a first for everything, right?
    """
    try:
        while True:
            countdown(WORK_TIME)  # Let's get to work first!
            countdown(BREAK_TIME)  # Yay - it's break time!

    except KeyboardInterrupt:  # A fine way of saying, "I need a longer break!"
        print('\n\nPomodoro Timer stopped. See you soon!')
        sys.exit(0)  # Gracefully exiting our program

if __name__ == "__main__":
    """
    I guess you're ready. So, let's run our Pomodoro Timer & enjoy a burst of Productivity! ;)
    """
    print('\nPomodoro Timer started. Let\'s get productive!')
    pomodoro_timer()

