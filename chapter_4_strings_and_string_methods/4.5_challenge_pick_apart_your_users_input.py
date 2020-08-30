# 4.5 Challenge: Pick Apart Your User's Input
# First Letter

""" Write a program named first_letter.py that prompts the user for input 
with the string "Tell me your password:" The program should then determine 
the first letter of the user’s input, convert that letter to uppercase, and 
display it back.
For example, if the user input is "no" , then the program should display 
the following output:
The first letter you entered was: N
For now, it’s okay if your program crashes when the user enters nothing as 
input—that is, when they just hit Enter instead of typing something. You’ll 
learn a couple of ways to deal with this situation in an upcoming chapter. """

password = input("Tell me your password: ")

password_first_letter = password[:1]
password_first_upper = password_first_letter.upper()

print("The first letter you entered was: " + password_first_upper)