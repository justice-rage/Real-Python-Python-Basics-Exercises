# 8.8 Challenge: Simulate a Coin Toss Experiment

""" Suppose you flip a fair coin repeatedly until it lands on both heads 
and tails at least once each. In other words, after the first flip, you 
continue to flip the coin until it lands on something different. Doing this
generates a sequence of heads and tails. For example, the first time you 
do this experiment, the sequence might be heads, heads, then tails.
On average, how many flips are needed for the sequence to contain both 
heads and tails?

Write a simulation that runs 10,000 trials of the experiment and prints
the average number of flips per trial. """

import random
from statistics import mean

def coin_flip():
    """Returns 'Heads' or 'Tails' randomly"""
    result = random.randint(1, 2)
    if result == 1:
        return "Heads"
    else:
        return "Tails"

ambos_sequence_tracker = [] # List logging number of flips it takes for both
                            # 'Heads' and 'Tails' to appear.

flips = 0

for trial in range(10_000):
    # Starts flips
    first_flip = coin_flip()
    flips = flips + 1
    # Continues flipping coin and updates tally until different
    # result is returned by coin_flips() .
    while coin_flip() == first_flip: 
        flips = flips + 1
    # Increment flip tally once more to account for the final flip
    # with different result.
    ambos_sequence_tracker.append(flips)
    flips = 1 # Resets flips to 1 to ensure list doesn't infinitely add flips

print(str(mean(ambos_sequence_tracker)))


