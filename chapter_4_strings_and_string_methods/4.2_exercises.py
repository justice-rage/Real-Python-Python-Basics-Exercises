# 4.2 Concatenation, Indexing, and Slicing

# 1) Create a string and print its length using len() .

var_1 = "How many characters am I?"
print(len(var_1))

# 2) Create two strings, concatenate them, and print the resulting string.

string_1 = "H"
string_2 = "i"
super_string = string_1 + string_2

print(super_string)

# 3) Create two strings, use concatenation to add a space between them,
# and print the result.

yin = "You"
yang = "complete me."
yin_and_yang = yin + " " + yang

print(yin_and_yang)

# 4) Print the string "zing" by using the slice notation to specify the
# correct range of characters in the string "bazinga".

slice_practice = "bazinga"
print(slice_practice[2:-1])