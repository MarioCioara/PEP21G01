# def my_func(arg1,arg2,agr3=1):
#     print(arg1,arg2,agr3)
#
# my_func('value1','value2')

# ex: print all primes in a range:

# def prime(max_prime):
#
#     my_primes = []
#     for number in range(1, max_prime + 1):
#         if number < 3:
#             #print(number, end=', ')
#             my_primes.append(number)
#             continue
#         for divider in range(2, number):
#             if number % divider == 0:
#                 break
#         else:
#             my_primes.append(number)
#             #print(number, end=', ')
#
#     return my_primes
#
# my_primes = prime(21)
# print('Primes are: ', my_primes)

# -----------------------------------------------------------


# liste


# my_list = [1, 2, 3]
# list_iter = my_list.__iter__()
# for number in my_list:
#     # print(number)


# number = 1
# print(id(number))
# number += 1
# print(id(number))
#
# my_list.append(4)
# print(my_list)
# print(id(my_list))
# print(my_list == [1,2,3,4])
# print(my_list == my_list.append(5))
# print(id(my_list), id(my_list.append(5)))
# print()
# new_object1 = 'my_str_{}'.format('1')
# print(new_object1)
# new_object2 = [1,2,3].append('1')
# print(new_object2)


# lista = 1
# print(type(lista) == str)
# print(type(lista) == list)

# exercitiu cu liste in liste

# data = [1, [2, [3]], 4, [5, [6]], 7, [8, [9]]]
#
# def flatten_list(complex_list):
#     flat_list = []
#     for obj_primary in complex_list:
#         if(type(obj_primary) == int):
#             flat_list.append(obj_primary )
#         else:
#             for obj_secondary in obj_primary:
#                 if(type(obj_secondary) == int):
#                     flat_list.append(obj_secondary)
#                 else:
#                     for obj_tertiary in obj_secondary:
#                         if(type(obj_tertiary) == int):
#                             flat_list.append(obj_tertiary)
#     return flat_list
#
# final_list = flatten_list(data)
# print(final_list)


# XOR

# print(10 & 10)
# print((10).__and__(10))

# print(11 ^ 10)
# print((11).__xor__(10))
# result = (11).__xor__(10)
# result = result.__xor__(10)
# print('Result: ',result)

# 1011 - 11
# 1010 - 10
# 0001 - 1

# text = "Éÿå°óñþðä°âõñô°äøùã"
# my_list = []
# for letter in text:
#     print(chr(ord(letter).__xor__(144)),sep="",end='')

# result = '-'.join(['word1','word2','x'])
#
# print(result)


# def encript(text,key):
#     my_list = []
#
#     for letter in text:
#         x = "".join(chr(ord(letter).__xor__(key)))
#         my_letter = chr(ord(letter).__xor__(key))
#         my_list.append(my_letter)
#     result = "".join(my_list)
#     return result
#
# enc = encript("Éÿå°óñþðä°âõñô°äøùã",144)
# print(enc)

# -------------------------------------------------------

# add numbers

# def add_numbers():
#     suma = 0
#     my_list = []
#     while (suma < 100):
#         number = int(input('enter number: '))
#         suma = suma + number
#         my_list.append(number)
#         if(suma>100):
#             return my_list
#     else:
#         return suma
#
#
# result = add_numbers()
# print(result)
