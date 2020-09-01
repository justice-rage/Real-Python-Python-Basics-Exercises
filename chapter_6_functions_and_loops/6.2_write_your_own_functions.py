# 6.2 Write Your Own Functions

# 1) Write a function called cube() with one number parameter and returns 
# the value of that number raised to the third power. Test the function by 
# displaying the result of calling your cube() function on a few different 
# numbers.

def cube(x):
    return (x ** 3)

num1 = input("Enter a number: ")

print(cube(int(num1)))

# 2) Write a function called greet() that takes one string parameter called
#  name and displays the text "Hello <name>!" , where <name> is replaced with
#  the value of the name parameter.

def greet(name):
    return(f"Hello {name}!")

name1 = input("Enter name: ")

print(greet(name1))

