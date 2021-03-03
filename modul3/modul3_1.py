# x = int(input())
# if(x<10):
#     print("Prea mic")
# elif x>10:
#     print("Prea mare")
# else:
#     print("Perfect")


# my_string = 'text'
# print(type(my_string))
# my_type = type(my_string)
# print(type(my_type))
#
# print(type(my_string) == str)
# print(type(my_type) == str)
#---------------------------------------------------
# x = str(input('x = '))
#
# if 47 < ord(x[0]) < 58:
#     print('x can be converted in int')
#     x = int(x)
#     print(type(x))
# else:
#     print("x can't be converted")

# x = input('X = ')
#
# if(type(x) == str):
#     print("Success")
# else:
#     print("Fail")

#-----------------------------------------------------------

# for letter in 'my_text':
#     print('Letter is: ',letter)

# str_iter = 'my_text'.__iter__()
#
# print(type(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
#----------------------------------------------

# n = int(input("n = "))
# for number in range(1,n+1):
#     if number<3:
#         print(f"{number} este prim")
#         continue
#     for i in range(2,number):
#         if number % i == 0:
#             print(f"{number} nu este prim")
#             break
#     else:
#          print(f"{number} este prim")


#---------------------------------------------------

x = str(input("text = "))

for i in x:
    print(chr(ord(i) + 129),sep='',end='')





