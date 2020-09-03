# 6.5 Challenge: Track Your Investments

""" In this challenge, you’ll write a program called invest.py that tracks 
the growing amount of an investment over time.
An initial deposit, called the principal amount, is made. Each year, the 
amount increases by a fixed percentage, called the annual rate of return.
For example, a principal amount of $100 with an annual rate of return of 
5% increases the first year by $5. The second year, the increase is 5% of
the new amount $105, which is $5.25.
Write a function called invest with three parameters: the principal amount, 
the annual rate of return, and the number of years to calculate. The function
signature might look something like this:
def invest(amount, rate, years):
The function then prints out the amount of the investment, rounded to 2 decimal
 places, at the end of each year for the specified number of years.
For example, calling invest(100, .05, 4) should print the following:
year 1: $105.00
year 2: $110.25
year 3: $115.76
year 4: $121.55
To finish the program, prompt the user to enter an initial amount, an annual 
percentage rate, and a number of years. Then call invest() to display the 
calculations for the values entered by the user. """

# invest.py code

def invest(amount, rate, years):
    """Display yearly growth of investment"""
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"Year {year}: ${amount:,.2f}")

amount = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate: "))
years = int(input("Enter number of years: "))

invest(amount, rate, years)
