# 4.8 Find a String in a String

# 1) In one line of code, display the result of trying to .find() the 
# substring "a" in the string "AAA" . The result should be -1 .

find_practice = "AAA"

print(find_practice.find("a"))

# 2) Replace every occurrence of the character "s" with "x" in the string
# "Somebody said something to Samantha."

replace_practice = "Somebody said something to Samantha."

print(replace_practice.replace("s", "x"))

# 3) Write a program that accepts user input with input() and displays the 
# result of trying to .find() a particular letter in that input.

variable = input("Input a word: ")
particular_letter_location = variable.find("a")

print(particular_letter_location)