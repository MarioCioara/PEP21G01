# We want to check which of the following function has the smallest minimum for x in range -10, 10 and use that function
# to calculate for x = 0
# 1x^2 -2x + 2
# 2x^2 -4x + 4
# 3x^2 -6x + 6

# 20P
# Create a function (build) that takes 3 int arguments (a, b, c) and return a function (response) that takes one int
# argument (x) and calculates ax^2+bx+c

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
x = int(input('x = '))

def build(a, b, c):    # the first function
    def response(x):   # the second function which is returned by the first function
        result = 0
        result = a * x ** 2 + b * x + c # we do the calculus
        print('Result = ' + str(result))  # we print the result of the calculus
    return response    # we return the out second function inside the first function

function = build(a,b,c) # we store the first function in a variable
function(x) # our variable now can call the second function and print the result






