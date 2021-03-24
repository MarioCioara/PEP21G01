# def divide(number,divider):
#     try:
#         raise AttributeError()
#         result = number / divider
#     except ZeroDivisionError:
#         return None
#     except AttributeError:
#         print('This is an AttributeError')
#         result = None
#     return result
#
# print(divide(2,0))

# def divide(number,divider):
#     try:
#
#         if number == 0:
#             raise Exception
#
#         result = number / divider
#     except ZeroDivisionError:
#         print('This is a ZeroDivisionError')
#         return None
#     except Exception:
#         print('This is an Exception')
#         return None
#
#     except AttributeError:
#         print('This is an AttributeError')
#         result = None
#     return result
#
# print(divide(2,0))
# print('The End')

#-------------------------------------------------------------------

#sortarea listei in ordine crescatoare

# list1 = [1,10,-2,'-100',None,{}]
#
# def compare(list):
#     new_list = []
#     for element in list:
#         if not new_list:
#             new_list.append(element)
#             continue
#         for obj in new_list.copy():
#             try:
#                 result = element < obj
#             except TypeError as e:
#                 print(e.args[0].split("'")[3])
#                 if e.args[0].split("'")[3] == 'str':
#                     element = int(element)
#
#
#                 elif e.args[0].split("'")[3] == 'dict':
#
#                     element = len(element)
#
#
#                 elif e.args[0].split("'")[3] == 'NoneType':
#                     element = len(str(element))
#
#
#                 else:
#                     continue
#
#
#             if element < obj:
#
#                 new_list.insert(new_list.index(obj), element)
#                 break
#         else:
#             new_list.append(element)
#
#     print(new_list)
# compare(list1)

#-----------------------------------------------------------------------------------

var1 = None
var2 = None
var3 = None

def read_input(v1,v2,v3):
    global var1,var2,var3

    try:
        var1 = int(input('var1 = '))
        var2 = int(input('var2 = '))
        var3 = int(input('var3 = '))
        sum = var1 + var2 + var3
    except:
        var1,var2,var3 = None,None,None
    else:
        var1,var2,var3 = sum,sum,sum
    finally:
        try:
            sum
        except UnboundLocalError:
         sum = 0

#cum vedem daca exista o variabila


    return sum

print(read_input(var1,var2,var3))
print(var1,var2,var3)