# 25P
# Write a function that will calculate factorial of numbers squared.
# For n = 3 the function should calculate (1^2)*(2^2)*(3^2)

x = int(input('x = '))

def factorial_of_squares(fact):
    p = 1
    for y in range(1,fact+1):
        p = p * y.__pow__(2)
    return p



print('Factorial de x este: ',factorial_of_squares(x))