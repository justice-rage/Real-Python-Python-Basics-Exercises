import random


def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


flips = 0
num_trials = 10_000

for trial in range(num_trials):
    if coin_flip() == "heads":
        # Increment the number of flips by 1
        flips = flips + 1
        while coin_flip() == "heads":
            # Keep incrementing the total number of flips
            # until "tails" is returned by coin_flip()
            flips = flips + 1
        # Once coin_flip() return "tails", the loop will exit,
        # but we need to add one more to flips to track the
        # last flip that generated "tails"
        flips = flips + 1
    else:
        # coin_flip() returned "tails" on the first flip.
        # Increment the number of flips by 1
        flips = flips + 1
        while coin_flip() == "tails":
            # Keep incrementing the total number of flips
            # until "heads" is returned by coin_flip()
            flips = flips + 1
        # Once coin_flip() returns "heads", the loop will exit,
        # but we need to add one more to flips to track the
        # last flip that generated "heads"
        flips = flips + 1

avg_flips_per_trial = flips / num_trials
print(f"{avg_flips_per_trial}.")