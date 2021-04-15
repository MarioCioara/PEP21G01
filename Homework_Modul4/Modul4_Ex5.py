# 20P
# Call function_with_smallest_result with argument x = 0 and print the returned value (you should get 2)

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


function_with_smallest_result = None
smallest_value = None
list_min_values = []
for function, values in dict_of_results.items():
    list_min_values.append(min(values))
    smallest_value = min(list_min_values)
    for element in values:
        if(min(list_min_values) == element):
            function_with_smallest_result = function


print(function_with_smallest_result(0))

































