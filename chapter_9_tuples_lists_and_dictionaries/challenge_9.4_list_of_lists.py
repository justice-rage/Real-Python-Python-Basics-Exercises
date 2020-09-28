# Challenge 9.4 List of Lists

# Write a program that contains the following lists of lists:
# universities = [    ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],    ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],    ['Rice', 5879, 35551],    ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]    ]

""" Define a function, enrollment_stats() , that takes, as an input, a list
of lists where each individual list contains three elements: (a) the name 
of a university, (b) the total number of enrolled students, and (c) the 
annual tuition fees.

enrollment_stats() should return two lists: the first containing all of the
student enrollment values and the second containing all of the tuition fees.
Next, define a mean() and a median() function. Both functions should take a
single list as an argument and return the mean and median of the values in 
each list.

Using universities , enrollment_stats() , mean() , and median() , calculate 
the total number of students, the total tuition, the mean and median of the 
number of students, and the mean and median tuition values.
Finally, output all values, and format the output so that it looks like this:

******************************
Total students: 77,285 Total tuition: $271,905 Student mean: 11,040.71 
Student median: 10,566 Tuition mean: $38,843.57 Tuition median: $ 39,849
****************************** """

# Imported mean and median functions instead of hand creating
from statistics import mean, median

def enrollment_stats(university_list):
    # Variables
    total_students = []
    total_tuition = []

    # Iterate through lists, adding values
    for university in university_list:
        total_students.append(university[1])
        total_tuition.append(university[2])

    # Return variables
    return total_students, total_tuition

# list of lists
universities = [ ['California Institute of Technology', 2175, 37704], ['Harvard', 19627, 39849], 
['Massachusetts Institute of Technology', 10566, 40732], ['Princeton', 7802, 37000], ['Rice', 5879, 35551],
['Stanford', 19535, 40569], ['Yale', 11701, 40500] ]

totals = enrollment_stats(universities)

print(f"Total students: {sum(totals[0]):,} \nTotal tuition: ${sum(totals[1]):,.2f} \n")
print(f"Student mean: {mean(totals[0]):,.2f} \nStudent median: {median(totals[0]):,} \n")
print(f"Tuition mean: ${mean(totals[1]):,.2f} \nTuition median: ${median(totals[1]):,.2f} \n")