# 8.2 Add Some Logic

# 1) Figure out what the result will be ( True or False ) when evaluating
#  the following expressions, then type them into the interactive window 
# to check your answers:

(1 <= 1) and (1 != 1) # Guess: False
not (1 != 2) # Guess: False
("good" != "bad") or False # Guess: True
("good" != "Good") and not (1 == 1) # Guess: False

# 2) Add parentheses where necessary so that each of the following 
# expressions evaluates to True :

False == not True # False == (not True)
True and False == True and False # True and False == (True and False)
not True and "A" == "B" # not (True and "A" == "B")