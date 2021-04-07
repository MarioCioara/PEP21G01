# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have their length counted
# The function will return a list with a int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]

data = [1,True,'123',False,6,()]


def ordered_ints(work_data):
    new_data = []                # A empty list that will be filled with new data
    for x in work_data:
        if type(x) == int:
            new_data.append(x)    # We check to see if x is already an int,and if it's true than we will add x to the new list
        elif type(x) == str:
            new_data.append(int(x))
        elif type(x) == bool:         # If x is a bool then we will add to the list 1 for True and 0 for False
            if x == True:
                new_data.append(1)
            else:
                new_data.append(0)
        else:
            new_data.append(len(x))  # If x can't be converted into int than we add the length of x to the list




    return sorted(new_data, reverse=True) # Reverse sorting our new list



print(ordered_ints(data))