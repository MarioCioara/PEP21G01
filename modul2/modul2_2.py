#slice

string1 = 'My string'
result = string1[0]
print(result)

result = string1[0:5]
print(result)
print()
result = string1[4:8]
print(result)
print()
result = string1[-5:-1]
print(result)
print()
result = string1[0:8:2]
print(result)
print()

encode = 'My text to encode'
decode = encode[5:] + encode[0:5]
print(decode)
decode = decode[-5:] + decode[:-5]
print(decode)
print()

result = encode[::-1]
print('Reverse: ',result)
print()

decode = encode[-1:-10:-1] + encode[-10::-1]
print(decode)
decode = decode[:10:-1]  + decode[10::-1]
print(decode)
print()

# chr , ord

print(chr(400))
print()
print(ord('d'))

print('abc' > 'abd')
print()

encode = 'abc'
result = chr(ord(encode[0]) + 1) + chr(ord(encode[1]) + 1) + chr(ord(encode[2]) + 1)
print(result)


# cast

print(ord('1'))

print(int('1'))
print(type(int('1')))

# ex: time difference

start_time = '22:30'
end_time = '30:10'

start1 = int(start_time[0:2])

start2 = int(start_time[3:])
end1 = int(end_time[0:2])
end2 = int(end_time[3:])

total1 = (start1 * 60) + start2
total2 = (end1 * 60) + end2

diff = total2 - total1
print(diff)

# input

#input('Enter text here: ')

#start_time = str(input('start_time: '))
#end_time = str(input('end_time: '))

start1 = int(start_time[0:2])

start2 = int(start_time[3:])
end1 = int(end_time[0:2])
end2 = int(end_time[3:])

total1 = (start1 * 60) + start2
total2 = (end1 * 60) + end2

diff = total2 - total1


#my_input = float(input("Enter your number: "))
#print(my_input)
#my_input = complex(input("Enter your number: "))
#print(my_input)

# None

# print(None)

# bool object

# print(True)
# print(False)
#
# print(id(None), id(True), id(False))
# print()
#ex: > < >= <= == !=

#a = str(input('a = '))
#b = str(input('b = '))

#print('a > b: ',a > b)
#print('a < b: ',a < b)
#print('a >= b: ',a >= b)
#print('a <= b: ',a <= b)
#print('a == b: ',a == b)
#print('a != b: ',a != b)

# print('a > b: ',a.__gt__(b))
# print('a < b: ',a.__lt__(b))
# print('a >= b: ',a.__ge__(b))
# print('a <= b: ',a.__le__(b))
# print('a == b: ',a.__eq__(b))
# print('a != b: ',a.__ne__(b))

# var1 = '/abc/\n'
# var2 = '/' + 'a' + 'b' + 'c' + '/\n'


# print('IS',var1 is var2)
# print('==', var1 == var2)
# print(id(var1),id(var2))

# exercitiu
print('/'.center(20,' '))
print('/'.center(18,' '))
print('/'.center(16,' '))
print('/'.center(14,' '))
print('/'.center(12,' '))
print('/'.center(10,' '))
print('/'.center(8,' '))
print('/'.center(6,' '))
print('/'.center(4,' '))
print('/'.center(2,' '))

