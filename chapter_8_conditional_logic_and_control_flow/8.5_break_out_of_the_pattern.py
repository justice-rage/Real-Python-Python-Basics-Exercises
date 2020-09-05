# 8.5 Break Out of the Pattern

# 1) Using break, write a program that repeatedly asks the user for some
# input and only quits if the user enters "q" or "Q".

while True:
    user_input = input("Input 'Q' to terminate program: ")
    if user_input.upper() == "Q":
        break

# 2) Using continue, write a program that loops over the numbers 1 to 50
# and prints all numbers that are not multiples of 3.

for i in range(51):
    if i % 3 == 0:
        continue
    print(i)
