# 20P
# Create a list of response functions by calling build function with the arguments (1,-2,3), (2,-4,4), (3,-6,5)

def build(a, b, c):
    def response(x):
        result = 0
        result = a * x ** 2 + b * x + c
        return result
    return response

list_of_functions = []

for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):
    list_of_functions.append(build(a,b,c))

print('List of response functions = ',list_of_functions)


# Nu stiu sigur daca am facut bine aici.Tinand cont ca nu am primit valori si pentru x atunci am trecut in lista functiile
# propriu-zise nu result-ul fiecarei functii response