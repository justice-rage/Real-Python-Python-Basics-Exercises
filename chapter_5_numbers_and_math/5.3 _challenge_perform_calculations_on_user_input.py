# 5.3 Challenge: Perform Calculations on User Input

""" Write a script called exponent.py that receives two numbers from the 
user and displays the first number raised to the power of the second number.
A sample run of the program should look like this (with example input that 
has been provided by the user included below):
Enter a base: 1.2
Enter an exponent: 3
1.2 to the power of 3 = 1.7279999999999998

Keep the following in mind:
1.  Before you can do anything with the user’s input, you will have to assign both calls to input() to new variables.
2.  The input() function returns a string, so you’ll need to convert the user’s input into numbers in order to do arithmetic.
3.  You can use an f-string to print the result.
4.  You can assume that the user will enter actual numbers as input. """

# exponent.py script

base = input("Enter a base: ")
exponent = input("Enter an exponent: ")

raised_base = float(base) ** float(exponent)

print(f"{base} to the power of {exponent} = {raised_base}")

