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

noun = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verb = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adj = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"] # adjectives
prep = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"] # prepositions
adv = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"] # adverbs
article = ["a", "an"]

def poem_creator():
    """ Radnomly selects appropriate word types for poem construction. """
    # Chooses 3 different nouns
    noun1 = random.choice(noun)
    noun2 = random.choice(noun)
    noun3 = random.choice(noun)
    # Ensures different nouns are selected
    while noun1 == noun2:
        noun2 = random.choice(noun)
    while noun3 == noun1 or noun2:
        noun3 == random.choice(noun)

    # Chooses 3 different verbs
    verb1 = random.choice(verb)
    verb2 = random.choice(verb)
    verb3 = random.choice(verb)
    # Ensures different verbs are selected
    while verb1 == verb2:
        verb2 = random.choice(verb)
    while verb3 == verb1 or verb2:
        verb3 == random.choice(verb)

     # Chooses 3 different adjectives
    adj1 = random.choice(adj)
    adj2 = random.choice(adj)
    adj3 = random.choice(adj)
    # Ensures different adjectives are selected
    while adj1 == adj2:
        adj2 = random.choice(adj)
    while adj3 == adj1 or adj2:
        adj3 == random.choice(adj)

    # Chooses 2 different prepositions
    prep1 = random.choice(prep)
    prep2 = random.choice(prep)
    while prep1 == prep2:
        prep2 = random.choice(prep)

    # Choose 1 adverb
    adv1 = random.choice(adv)

    # Chooses appropriate article
    if "aeiou".find(adj1[0]) != -1:  # First letter is a vowel
        article = "An"
    else:
        article = "A"

    # Create the poem
    poem = (
        f"{article} {adj1} {noun1}\n\n"
        f"{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}\n"
        f"{adv1}, the {noun1} {verb2}\n"
        f"the {noun2} {verb3} {prep2} a {adj3} {noun3}"
    )

    return poem

poem = poem_creator()
print(poem)