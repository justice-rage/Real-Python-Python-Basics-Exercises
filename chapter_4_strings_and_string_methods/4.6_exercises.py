# 4.6 working With Strings and Numbers

# 1) Create a string containing an integer, then convert that string into
# an actual integer object using int() . Test that your new object is a 
# number by multiplying it by another number and displaying the result.

string_number = "2"
print(int(string_number) * 3)

# 2) Repeat the previous exercise, but use a floating-point number and 
# float() .

print(float(string_number) * 3)

# 3) Create a string object and an integer object, then display them 
# side by side with a single print statement using str() .

string_obj = "My favorite number is "
integer_obj = 13
single_statement = string_obj + str(integer_obj)

print(single_statement)

# 4) Write a program that uses input() twice to get two numbers from 
# the user, multiplies the numbers together, and displays the result. 
# If the user enters 2 and 4, your program should print the following 
# text: The product of 2 and 4 is 8.0.

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

num_product = float(num1) * float(num2)

print("The product of " + num1 + " and " + num2 + " is " + str(num_product) + ".")