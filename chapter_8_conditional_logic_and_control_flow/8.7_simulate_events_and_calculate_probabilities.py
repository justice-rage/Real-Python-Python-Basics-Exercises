# 8.7 Simulate Events and Calculate Probabilities

import random

# 1) Write a function called roll() that uses the randint() function to 
# simulate rolling a fair die by returning a random integer between 1 and 6 .

def roll():
    """Return random integer between 1-6"""
    return randint(1, 6)

# 2) Write a program that simulates 10,000 rolls of a fair die and displays 
# the average number rolled.
