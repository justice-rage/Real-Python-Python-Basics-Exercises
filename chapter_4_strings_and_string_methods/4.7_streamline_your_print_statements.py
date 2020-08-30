# 4.7 Streamline Your Print Statements

# 1) Create a float object named weight with the value 0.2, and create a 
# string object named animal with the value "newt" . Then use these objects
# to print the following string using only string concatenation:
# 0.2 kg is the weight of the newt.

weight = 0.2
animal = "newt"

print(str(weight) + " kg is the weight of the new " + animal + ".")

# 2) Display the same string by using .format() and empty {} placeholders.

print("{} kg is the weight of the new {}.".format(weight, animal))

# 3) Display the same string using an f-string.

print(f"{weight} kg is the weight of the new {animal}.")