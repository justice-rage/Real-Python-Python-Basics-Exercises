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
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


flips = 0
num_trials = 10_000

# empty list utilized for appending flips
avg_per_trial = []

for trial in range(num_trials):
    # Flip the coin once and increment the flips tally by 1
    first_flip = coin_flip()
    flips = flips + 1
    # Continue flipping the coin and updating the tally until
    # a different result is returned by coin_flips()
    while coin_flip() == first_flip:
        flips = flips + 1
    # Increment the flip tally once more to account for the
    # final flip with a different result
    flips = flips + 1

avg_per_trial.append(flips) # appends flips to

avg_flips_per_trial = mean(avg_per_trial) # Returns correct output without decimal
print(f"Average number of flips per trial: {avg_flips_per_trial}.")




