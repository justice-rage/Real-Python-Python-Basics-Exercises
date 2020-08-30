# 4.9 Challenge: Turn Your User Into a L33t H4x0r

""" Write a program called translate.py that asks the user for some input
 with the following prompt:
Enter some text:
Use .replace() to convert the text entered by the user into leetspeak by 
making the following changes to lowercase letters:
•  The letter a becomes 4
•  The letter b becomes 8
•  The letter e becomes 3
•  The letter l becomes 1
•  The letter o becomes 0
•  The letter s becomes 5
•  The letter t becomes 7
Your program should then display the resulting string as output. Below is 
a sample run of the program:
Enter some text: I like to eat eggs and spam.
I 1ik3 70 347 3gg5 4nd 5p4m. """

some_text = input("Enter some text: ")

some_text = some_text.replace("a", "4")
some_text = some_text.replace("b", "8")
some_text = some_text.replace("e", "3")
some_text = some_text.replace("l", "1")
some_text = some_text.replace("o", "0")
some_text = some_text.replace("s", "5")
some_text = some_text.replace("t", "7")

print(some_text)
