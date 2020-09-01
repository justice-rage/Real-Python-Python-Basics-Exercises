# 5.5 Math Functions and Number Methods

# 1) Write a script that asks the user to input a number and then displays
# that number rounded to two decimal places. When run, your program should 
# look like this:

""" Enter a number: 5.432
5.432 rounded to 2 decimal places is 5.43 """

num1 = input("Enter a number: ")
num1_rounded = round(float(num1), 2)

print(f"{num1} rounded to 2 decimal places is {num1_rounded}")

# 2) Write a script that asks the user to input a number and then displays 
# the absolute value of that number. When run, your program should look like 
# this:

""" Enter a number: -10
The absolute value of -10 is 10.0 """

num2 = input("Enter a number: ")
num2_abs = abs(float(num2))

print(f"The absolute value of {num2} is {num2_abs}")

# 3) Write a script that asks the user to input two numbers by using the 
# input() function twice, then display whether or not the difference between
# those two number is an integer. When run, your program should look 
# like this:

""" Enter a number: 1.5
Enter another number: .5
The difference between 1.5 and .5 is an integer? 
True! """

# If the user inputs two numbers whose difference is not integral, the output 
# should look like this:

"""Enter a number: 1.5
Enter another number: 1.0
The difference between 1.5 and 1.0 is an integer? 
False! """

num4 = input("Enter a number: ")
num5 = input("Enter another number: ")

int_dif = float(num4) - float(num5)

print(f"The difference between {num4} and {num5} is an integer?")
print(int_dif.is_integer())

