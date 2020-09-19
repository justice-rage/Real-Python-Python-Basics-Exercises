# 9.1 Tuples are Immutable Sequences

# 1) Create a tuple literal named cardinal_numbers that holds the strings 
# "first" , "second" and "third" , in that order.

cardinal_numbers = ("first", "second", "third")

# 2) Using index notation and print() , display the string at index 1 in 
# cardinal_numbers .

print(cardinal_numbers[1])

# 3) Unpack the values in cardinal_numbers into three new strings named 
# position1 , position2 and position3 in a single line of code, then print 
# each value on a separate line.

postion1, postion2, position3 = cardinal_numbers
print(f"{postion1}\n{postion2}\n{position3}")

# 4) Create a tuple called my_name that contains the letters of your name 
# by using tuple() and a string literal.

my_name = tuple("Justice")

# 5) Check whether or not the character "x" is in my_name using the 
# in keyword.

print("x" in my_name)

# 6) Create a new tuple containing all but the first letter in my_name 
# using slicing notation.

print(my_name[1:])