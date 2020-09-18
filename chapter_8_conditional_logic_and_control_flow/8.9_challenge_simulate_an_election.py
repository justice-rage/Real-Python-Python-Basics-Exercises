# 8.9 Challenge: Simulate an Election

""" With some help from the random module and a little condition logic,
you can simulate an election between two candidates.
Suppose two candidates, Candidate A and Candidate B, are running for mayor
in a city with three voting regions. The most recent polls show that 
Candidate A has the following chances for winning in each region:
 •  Region 1: 87% chance of winning
 •  Region 2: 65% chance of winning
 •  Region 3: 17% chance of winning
Write a program that simulates the election 10,000 times and prints the 
percentage of where Candidate A wins.
To keep things simple, assume that a candidate wins the election is they
win in at least two of the three regions.
"""

from random import random

candidate_a_wins = 0
candidate_b_wins = 0

region_1 = .87
region_2 = .65
region_3 = .17

election_simulations = 10_000

for trials in range(election_simulations):
    a_votes = 0
    b_votes = 0

    # determines 1st region results
    if random() < .87:
        a_votes = a_votes + 1
    else:
        b_votes = b_votes + 1

    # determines 2nd region results
    if random() < .65:
        a_votes = a_votes + 1
    else:
        b_votes = b_votes + 1

    # determines 3rd region results
    if random() < .17:
        a_votes = a_votes + 1
    else:
        b_votes = b_votes + 1

    # determines overall election outcome
    if a_votes > b_votes:
        candidate_a_wins = candidate_a_wins + 1
    else:
        candidate_b_wins = candidate_b_wins + 1

a_results = (candidate_a_wins/election_simulations)
b_results = (candidate_b_wins/election_simulations)

print(f"Candidate A percentage: {a_results:.0%}")
print(f"Candidate A percentage: {b_results:.0%}")