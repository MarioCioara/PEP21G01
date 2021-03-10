#dictionare

# my_dict = {
#     'key1': 'value1',
#     1: '1',
#     None: print,
#     (1,2): 'list'
#
# }

# for key in my_dict.keys():
#     print('keys: ',key)
# print()
# for value in my_dict.values():
#     print('values: ',value)

# for key, value in my_dict.items():
#     print(key, value)



#Vrem sa aflam magazinul cu cele mai bune preturi
# shop1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20} #produs : pret
# shop2 = {'mere': 11, 'pere': 15, 'prune': 6} #produs : pret
# shop3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25} #produs : pret
#
# need_to_buy = {'mere': 2, 'pere': 3, 'prune': 6} #produs : cantitate
#
# available_shops = {'a': shop1, 'b': shop2, 'c': shop3}
#
# def best_buy(available_shops,need_to_buy):
#     min_price = None
#     nume_magazin=''
#     for shop_name,content in available_shops.items():
#         suma1 = 0
#         for product,quantity in need_to_buy.items():
#             suma1 = content.get(product) * quantity
#
#         print('Suma partiala in',shop_name,'=',suma1)
#         if min_price is None or min_price > suma1:
#             min_price=suma1
#             nume_magazin = shop_name
#
#
#     print(min_price)
#     print(nume_magazin)

# best_buy(available_shops=available_shops,need_to_buy=need_to_buy)


#------------------------------------------------------------------------------------------

# def down(nr):
#     nr = nr - 1
#     if nr>0:
#         return down(nr)
#     else:
#         return nr
#
# print(down(10))

#----------------------------------------------------------------------

#Flat list recursiv

# data = [1, [2, [3]], 4, [5, [6]], 7, [8, [9]]]
#
#
# def flatten_list(complex_list):
#     flat_list = []
#     for obj_primary in complex_list:
#         if(type(obj_primary) == list):
#             result = flatten_list(obj_primary )
#             flat_list.extend(result)
#         else:
#             flat_list.append(obj_primary)
#
#     return flat_list
#
# final_list = flatten_list(data)
# print('Final list is: ',final_list)

#------------------------------------------------------------------------------

#Return a list with the names that have the sum of the number > 50

my_dict = {'Ana': 762399332,'Adi': 723432145,'Bogdan': 750567987}

def return_name(dict):
    lista = []
    for nume,nr in dict.items():
        s = 0
        for cifra in str(nr):
            s = s + int(cifra)
        if (s > 50):
            lista.append(nume)
    return lista

print(return_name(my_dict))


