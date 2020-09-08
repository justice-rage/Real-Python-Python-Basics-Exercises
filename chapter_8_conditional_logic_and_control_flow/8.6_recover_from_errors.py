# 8.6 Recover From Errors

# 1) Write a program that repeatedly asks the user to input an integer, 
# displaying a message to “try again” by catching the ValueError that 
# is raised if the user did not enter an integer.
# Once the user enters an integer, the program should display the number
# back to the user and end without crashing.

while True:
    try:
        integer_input = int(input("Enter integer: "))
        print(integer_input)
        break
    except ValueError:
        print("Try again.")


# 2) Write a program that asks the user to input a string and an integer n. 
# Then display the character at index n in the string.
# Use error handling to make sure the program doesn’t crash if the user does
# not enter an integer or the index is out of bounds. The program should 
# display a different message depending on what error occurs.

string_var = str(input("Enter string: "))

while True:    
    try:
        index = int(input("Enter integer: "))
        print(string_var[index])
        break
    except ValueError:
        print("Error. Enter integer below. ")
    except IndexError:
        print("Error. Index out of bounds. Enter another below. ")

