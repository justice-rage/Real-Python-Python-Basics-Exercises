# 6.4 Run in Circles

# 1) Write a for loop that prints out the integers 2 through 10, each on a 
# new line, by using the range() function.

for x in range(2, 11):
    print(x)
    x = x + 1

# 2) Use a while loop that prints out the integers 2 through 10 
# (Hint: You’ll need to create a new integer first.)

y = 2
while y < 11:
    print(y)
    y = y + 1

# 3) Write a function called doubles() that takes one number as its input 
# and doubles that number. Then use the doubles() function in a loop to 
# double the number 2 three times, displaying each result on a separate line. 
# Here is some sample output:
# 4
# 8
# 16

def doubles(z):
    """ Takes one number as its input and doubles it. """
    return(z * 2)

n = 2
for i in range(0, 3):
    n = doubles(n)
    print(n)
