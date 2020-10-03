# 9.5 Challenge: Wax Poetic

""" In this challenge, you’ll write a program that generates poetry.
 Create five lists for different word types:
 •  Nouns: ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"] 
 •  Verbs: ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"] 
 •  Adjectives: ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"] 
 •  Prepositions: ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"] 
 •  Adverbs: ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"] 
 
 Randomly select the following number of elements from each list:
 •  3 nouns
 •  3 verbs
 •  3 adjectives
 •  2 prepositions
 •  1 adverb

You can do this with the choice() function in the random module. This function
takes a list as input and returns a randomly selected element of the list.
For example, here’s how you use random.choice() to get random element from
the list ["a", "b", "c"] :

import random
random_element = random.choice(["a", "b", "c"]) 

Using the randomly selected words, generate and display a poem with the following 
structure inspired by Clifford Pickover :
{A/An} {adj1} {noun1}{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} 
{noun2}{adverb1}, the {noun1} {verb2}the {noun2} {verb3} {prep2} a {adj3} 
{noun3} 

Every time your program runs, it should generate a new poem. """

import random

noun = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verb = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles",
]
adjective = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
]
preposition = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverb = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously",
]


def make_poem():
    """Create a randomly generated poem, returned as a multi-line string."""
    # Pull three nouns randomly
    n1 = random.choice(noun)
    n2 = random.choice(noun)
    n3 = random.choice(noun)
    # Make sure that all the nouns are different
    while n1 == n2:
        n2 = random.choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = random.choice(noun)

    # Pull three different verbs
    v1 = random.choice(verb)
    v2 = random.choice(verb)
    v3 = random.choice(verb)
    while v1 == v2:
        v2 = random.choice(verb)
    while v1 == v3 or v2 == v3:
        v3 = random.choice(verb)

    # Pull three different adjectives
    adj1 = random.choice(adjective)
    adj2 = random.choice(adjective)
    adj3 = random.choice(adjective)
    while adj1 == adj2:
        adj2 = random.choice(adjective)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = random.choice(adjective)

    # Pull two different prepositions
    prep1 = random.choice(preposition)
    prep2 = random.choice(preposition)
    while prep1 == prep2:
        prep2 = random.choice(preposition)

    # Pull one adverb
    adv1 = random.choice(adverb)

    if "aeiou".find(adj1[0]) != -1:  # First letter is a vowel
        article = "An"
    else:
        article = "A"

    # Create the poem
    poem = (
        f"{article} {adj1} {n1}.\n\n"
        f"{article} {adj1} {n1} {v1} {prep1} the {adj2} {n2}.\n"
        f"{adv1}, the {n1} {v2}.\n"
        f"the {n2} {v3} {prep2} a {adj3} {n3}."
    )

    return poem


poem = make_poem()
print(poem)