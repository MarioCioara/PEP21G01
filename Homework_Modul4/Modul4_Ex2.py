# 20P
# Create a list of response functions by calling build function with the arguments (1,-2,3), (2,-4,4), (3,-6,5)


def build(a, b, c):    # the first function
    def response(x):   # the second function which is returned by the first function

        result = 0
        result = a * x ** 2 + b * x + c # we do the calculus
        print('Result = ' + str(result))  # we print the result of the calculus
    return response    # we return the out second function inside the first function

# function = build(1,2,3) # we store the first function in a variable
# function(4) # our variable now can call the second function and print the result

list_of_functions = []

for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):


    list_of_functions.append(build(a,b,c))  # we append to the empty list the response functions

print('List of response functions = ',list_of_functions)


# Nu stiu sigur daca am facut bine aici.Tinand cont ca nu am primit valori si pentru x atunci am trecut in lista functiile
# propriu-zise nu result-ul fiecarei functii response