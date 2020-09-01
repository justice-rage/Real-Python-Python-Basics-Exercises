# 6.3 Challenge: Convert Temperatures

""" Write a program called temperature.py that defines two functions:
1. convert_cel_to_far() with one float parameter representing degrees 
Celsius and returns a float representing the same temperature in degrees
Fahrenheit using the following formula:
F = C * 9/5 + 32

2. convert_far_to_cel() with one float parameter representing degrees 
Fahrenheit and returns a float representing the same temperature in degrees
Celsius using the following formula:
C = (F - 32) * 5/9

The program should:
1. First, prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature converted to Celsius.
2. Then prompt the user to enter a temperature in degrees Celsius and display the temperature converted to Fahrenheit.
3. Display all converted temperatures rounded to 2 decimal places.

Here’s a sample run of the program:
Enter a temperature in degrees F: 72
72 degrees F = 22.22 degrees C
Enter a temperature in degrees C: 37
37 degrees C = 98.60 degrees F """

def convert_cel_to_far(c):
    return(c * 9/5 + 32)

def convert_far_to_cel(f):
    return((f-32) * 5/9)

# Fahrenheit to Celsius conversion
fahr_var = input("Enter temperature in degrees Fahrenheit: ")
print(f"{fahr_var} degrees F = {convert_far_to_cel(int(fahr_var)):.2f} degrees C")

# Celsius to Fahrenheit conversion
cel_var = input("Enter temperature in degrees Celsius: ")
print(f"{cel_var} degrees C = {convert_cel_to_far(int(cel_var)):.2f} degrees F")