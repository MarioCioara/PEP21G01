# variabile

number_3 = '3'
number_three = 3

print(number_3)
print(number_three)

# type

response = type(number_3)
print(response)

response = type(number_three)
print(response)

# integers

var1 = 123
print()
print('This is an integer:', type(var1))

# integer base

bin_number = 0b10
print()
print(bin_number)

oct_number = 0o10
print(oct_number)

hex_number = 0x10
print(hex_number)

# integer operations

print()
print('Sum of 2+8 is:', bin_number + oct_number)

# add method
print()
bin_number.__add__(oct_number)
print('Sum of 2+8 is:', bin_number.__add__(oct_number))
print('Sum of 2+8 is:', oct_number.__add__(bin_number))

# diff


# mult method
print('Multiplication 2 * 8: ', bin_number.__mul__(oct_number))
print()

# 3*3*3 with 2 methods
print(3 * 3 * 3)
print(number_three.__mul__(number_three.__mul__(number_three)))
print()

# raise to power

print('3 la puterea a 3-a: ', number_three.__pow__(3))
print('3 la puterea a 3-a: ', pow(number_three, number_three))
print('3 la puterea a 3-a: ', number_three ** 3)
print()

# division

print('Division')
print()
result = number_three / 3
print(result)
print(type(result))

print('True div: ', number_three.__truediv__(3))

# exercitiu


# cu operatii
a = 3
b = 4
c = 5
print()
x = (-b - ((b ** 2 - 4 * a * c) ** (1 / 2))) / (2 * a)
print(x)
print(type(x))
print()

#cu metode
_4ac = (4).__mul__(a.__mul__(c))
b_sqr = b.__pow__(2)
sqr_result = b_sqr.__sub__(_4ac)
sqrt_result = pow(sqr_result, (1).__truediv__(2))
minus_b = (0).__sub__(b)
# div_up = minus_b.__add__(sqrt_result)
div_up = sqrt_result.__add__(minus_b)
div_down = (2).__mul__(a)
result = div_up.__truediv__(div_down)
print(result)
print(type(result))
print()


# strings
print('---------------------------------------------------------------------')
string1 = 'My String'
print(string1)
print()
string2 = 'My String\nThis is a new line'
print(string2)
print()
string3 = """My String3
This is a new line
This is another new line"""
print(string3)
print()

# methods
print(string1 + string2)
print()
print(string1.__add__(string2))

#exercitiu
#write 'this is my code' 100 time

u = 'this is my code\n'
print(u * 100)
print(100 * u)
print(u.__mul__(100))
print((100).__mul__(u)) #this is not implemented so it will not run
print()
print('--------------------------------------------------------------------------')
#string types:
formatable_string = f'Start: {string1} End: {string2}'
print(formatable_string)
print()

nume = 'Cioara'
prenume = 'Mario'
string4 = f'Subsemnatul {nume} {prenume}\nDeclar: declaratie'
print(string4)
print('--------------------------------------------------------------------------------------')
print()

raw_string = r'\nThere is no new line\n2'
print(raw_string)

string5 = 'My String: {}'
result = string5.format('String Name')
print(result)
print()
string6 = 'Subsemnatul {} {}\nDeclar:declaratie'
result = string6.format('Cioara','Mario')
print(result)
print()
print()
result = string5.replace('{','(')
result = result.replace('}',')')
print(result)


