# 20P
# Create a dictionary that contains the result functions as keys and as values the list of results from calling that
# function with x in range -10, 10 as value


def build(a, b, c):
    def response(x):
        result = 0
        result = a * x ** 2 + b * x + c
        return result
    return response

list_of_functions = []
dict_of_results = {}


for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):
    list_of_functions.append(build(a,b,c))


for function in list_of_functions:
    list_values = []
    for y in range(-10, 10):

        list_values.append(function(y))
    dict_of_results[function] = list_values

print(dict_of_results)


































