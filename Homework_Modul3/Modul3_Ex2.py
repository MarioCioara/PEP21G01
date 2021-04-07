# 25P - (do not rush to resolve this)
# For recursive functions try reading the articles below if you find need more information
# https://realpython.com/python-thinking-recursively/
# https://www.python-course.eu/python3_recursive_functions.php
# After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2

nr_iter = int(input("Number of iterations = "))

def sum_of_square(iter):
    sum = 0
    for x in range(1,iter+1):
        sum = sum + x.__pow__(2)
    return sum



print("Sum = ",sum_of_square(nr_iter))