# #Pinball V1
#
# test_data = [[1,2,3],[3,3,5],[8,9,4],[2,8,4]]
#
# def func(data_set):
#     full_data = set()
#     set_test_data = set()
#     miss_data = set()
#     for z in range(1,11):
#         full_data.add(z)
#
#     for x in data_set:
#         for y in x:
#             set_test_data.add(y)
#
#     miss_data = full_data.difference(set_test_data)
#
#     return list(miss_data)
#
#
# print(func(test_data))

#Pinball V2

# test_data = [[1,2,3],[3,3,5],[8,9,4],[2,8,4]]
#
# def func(data_set):
#     full_data = set(range(1,11))
#     set_test_data = set()
#     for x in data_set:
#         set_test_data.update(set(x))
#
#     return list(full_data.difference(set_test_data))
#
# print(func(test_data))

#=-------------------------------------------------------------

# def wrapper():
#     name = "Sir" # This is not used
#     def conversation():
#         name = "Lady"
#
#         def hello():
#             nonlocal name
#             print(f"Hello {name}")
#
#         def question():
#             print(f"how is your day {name}?")
#         def response():
#             nonlocal name
#             name = input("My name is ")
#             print(f"My name is :{name}")
#         def age_qst():
#             print(f'How old are you,{name}?')
#         def age_rsp():
#
#             age = int(input())
#             print(f'I am {age}')
#         hello()
#         response()
#         question()
#         age_qst()
#         age_rsp()
#     conversation()
# wrapper()

#-----------------------------------------------------
# number = int(input('number = '))
# def factorial(nr):
#
#     fact = 1
#     for y in range(1,nr+1):
#         fact = fact * y
#     return fact
#
# print(factorial(number))


# def factorial(number):
#
#     if number <= 1:
#         return 1
#     else:
#         return number*factorial(number-1)
#
# print(factorial(3))

#factorial cu lista

# def factorial(number):
#     number = list(range(1, number+1))
#
#
#     if len(number) <= 1:
#         return 1
#     else:
#         return number[-1]*factorial(number[-2])
#
# print(factorial(3))


#---------------------------------------------------------------------------------------------------

#
# data = [1, [2, [3], {"a","b"}], 4, [5, [6], {"a":"a", "b":"b"}], 7, [8, [9, ("a", "b")]]]
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def flatten_list(complex_list):
#     flat_list=[]
#     for obj_primary in complex_list:
#         if type(obj_primary )==list:
#             result= flatten_list(obj_primary)
#             flat_list.extend(result)
#         elif type(obj_primary)==tuple:
#             result = flatten_list(obj_primary)
#             flat_list.extend(result)
#         elif type(obj_primary)==dict:
#             result = flatten_list(obj_primary)
#             flat_list.extend(result)
#         elif type(obj_primary)==set:
#             result = flatten_list(obj_primary)
#             flat_list.extend(result)
#         else:
#             flat_list.append(obj_primary)
#     return flat_list
# resoult=flatten_list(complex_list=data)
# print('Flat list:',resoult)

#----------------------------------------------------------------------------------------------

# data = [1, [2, [3,{'a','b'}]], 4, [5, [6,{'a':'a','b':'b'}]], 7, [8, [9,('a','b')]]]
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def flatten_list(complex_list):
#     flat_list = []
#     for obj_primary in complex_list:
#         if type(obj_primary) == str and len(obj_primary) == 1:
#             flat_list.append(obj_primary)
#         elif getattr(obj_primary, '__iter__', False):
#             result = flatten_list(obj_primary)
#             flat_list.extend(result)
#         else:
#             flat_list.append(obj_primary)
#     return flat_list
#
# print(flatten_list(data))