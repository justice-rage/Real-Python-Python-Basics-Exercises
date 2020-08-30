# 4.4 Interact With User Input

# 1) Write a program that takes input from  the user and displays that input
# back.

print(input("What's your favorite book? "))

# 2) Write a program that takes input from the user and displays the input
#  in lowercase.

word1 = input("What word do you want lower-cased? ")
print(word1.lower())

# 3) Write a program that takes input from the user and displays the number 
# of characters in the input.

word2 = input("Type a word: ")
print("There are " + str(len(word2)) + " charcters in the word " + word2 + ".")