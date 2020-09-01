# 5.1 Integers and Floating-Point Numbers

# 1) Write a script that creates the two variables, num1 and num2 . 
# Both num1 and num2 should be assigned the integer literal 25,000,000, 
# one written with underscored and one without. Print num1 and num2 on 
# two separate lines.

num1 = 25_000_000
num2 = 25000000

print(num1)
print(num2)

# 2) Write a script that assigns the floating-point literal 175000.0 to
# the variable num using exponential notation, and then prints num in 
# the interactive window.

num = 175e3
print(num)

# 3) In IDLE’s interactive window, try and find the smallest exponent N 
# so that 2e<N> , where <N> is replaced with your number, returns inf .

n = 2e308
print(n)