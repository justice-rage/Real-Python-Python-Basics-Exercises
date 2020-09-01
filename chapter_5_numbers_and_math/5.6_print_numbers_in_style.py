# 5.6 Print Numbers in Style

# 1) Print the result of the calculation 3 ** .125 as a fixed-point number with
# three decimal places.

x = 3 ** .125
print(f"{x:.3f}")

# 2) Print the number 150000 as currency, with the thousands grouped with commas. 
# Currency should be displayed with two decimal places.

y = 150_000
print(f"${y:,.2f}")

# 3) Print the result of 2 / 10 as a percentage with no decimal places. The 
# output should look like 20%

x = 2 / 10
print(f"{x:.0%}")

