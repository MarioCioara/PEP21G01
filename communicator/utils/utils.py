def prime(max_prime):

    my_primes = []
    for number in range(1, max_prime + 1):
        if number < 3:
            #print(number, end=', ')
            my_primes.append(number)
            continue
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            my_primes.append(number)
            #print(number, end=', ')

    return my_primes

#------------------------------------------------------------------

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