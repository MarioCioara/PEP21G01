#clase

#Print var

# class Test:
#     var = 'This is my text'
#     def method(self):
#         print(self.var)
#     def change_var(self):
#         self.var = 'This is another text'
#
# obj = Test()
# obj.method()
# obj.change_var()
# print('class variable = ',Test.var)
# print('Instance variable = ',obj.var)

#---------------------------------------------------------------


# class Test:
#     var = 'This is my text'
#     def method(self):
#         print(self.var)
#     def change_var(self):
#         self.var = 'This is another text'
#
# obj = Test()
# obj.method()
# obj.change_var()
# print('class variable = ',Test.var)
# print('Instance variable = ',obj.var)
# print()
# import random
# class Object2:
#     variable = [1,2,3]
#     def change_var(self):
#         self.variable.append(random.randint(1,100))
#
# obj2 = Object2()
# print('class variable = ',Object2.variable)
# print('Instance variable = ',obj2.variable)
# obj2.change_var()
# print()
# print('class variable = ',Object2.variable)
# print('Instance variable = ',obj2.variable)
# print()
# obj3 = Object2()
# print(obj3.variable)

#--------------------------------------------------------------------------------
#Numara cate obiecte au fost create

# class Cars:
#     counter = [0]
#     def __init__(self):
#         self.counter.insert(0,self.counter.pop(0)+1)
#
#
# car1 = Cars()
# car2 = Cars()
# car3 = Cars()
# car4 = Cars()
# print(car3.counter)
# print(Cars.counter)

#---------------------------------------------------------
#variabile private,mostenire

# class Conector:
#     __secret = None
#     def __init__(self, host, port):
#         self.port = port
#         self.host = host
#
# class Client(Conector):
#     pass
#
# class Server(Conector):
#     pass
#
# conector_obj = Conector('localhost',8080)
# client_obj = Client('localhost',9999)
# server_obj = Server('localhost',8888)
#
# print(client_obj.host,client_obj.port)
# print(server_obj.host,server_obj.port)
# print(client_obj._Conector__secret)
# print(server_obj._Conector__secret)

#----------------------------------------------------------------------
#schimbarea valorii unei variabile private

# class A:
#     __secret = 1
#
# class B(A):
#     def change(self):
#         self._A__secret = 100
#
# b = B()
# b.change()
# print(b._A__secret)

#------------------------------------------------------------------------
import socket
import random
def primes(max_prime):
    _primes = []
    for number in range(1, max_prime + 1):
        if number < 3:
            _primes.append(number)
            continue
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            _primes.append(number)
    return _primes
class Conector:
    __secret = None
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def generate_prime(self):
        mylist = list(filter(lambda nr: True if nr > 129 else False, primes(256)))
        # print(mylist)
        self.prime = mylist[random.randint(0, len(mylist) - 1)]
        # print(self.prime)
    def get_prime(self, prime):
        if not getattr(self, "prime", False):
            self.prime = prime

    def generate_base(self):
        if getattr(self, "prime", False):
            self.base = random.randint(2,self.prime-1)
    def get_base(self, base):
        if not getattr(self, "base", False):
            self.base = base


class Client(Conector):
    local_secret = None
    def generate_local_secret(self):
        self.local_secret = random.randint(2,self.prime)
        return pow(self.base, self.local_secret) % self.prime
    def get_secret(self,secret):
        self.secret = pow(secret, self.local_secret) % self.prime + 129
    def client_start(self):
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.bind((self.host,self.port))


class Server(Conector):
    local_secret = None

    def generate_local_secret(self):
        self.local_secret = random.randint(2, self.prime)
        return pow(self.base, self.local_secret) % self.prime
    def get_secret(self,secret):
        self.secret = pow(secret, self.local_secret) % self.prime + 129
    def server_start(self):
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.bind((self.host, self.port))
        listen = socket_server.listen(1)
        print(listen)



conector_obj = Conector("localhost", 8080)
client_obj = Client("localhost", 8081)
server_obj = Server("localhost", 8082)
client_obj.generate_prime()
client_obj.generate_base()
# server_obj.generate_prime()
server_obj.get_prime(client_obj.prime)
server_obj.get_base(client_obj.base)
print('Client:',client_obj.prime)
print('Server:',server_obj.prime)
print('Client - generate base:', client_obj.base)
print('Server - generate base:', server_obj.base)


client_s = client_obj.generate_local_secret()
server_s = server_obj.generate_local_secret()
print('Client secret: ',client_s)
print('Server secret: ',server_s)
client_obj.get_secret(server_s)
server_obj.get_secret(client_s)
print(client_obj.secret)
print(server_obj.secret)

print()
print(client_obj.host)
print(server_obj.port)
print(client_obj._Conector__secret) # -> asa se acceseaza un atribut privat. se mosteneste si in alte clase, dar il accesez folosind clasa principala.
print(server_obj._Conector__secret)
#extract random prime number between 129 and 256

print('#80#80')
client_obj.client_start()
print('-------')
server_obj.server_start()
print('########')

# var = primes(max_prime=256)
# def select(nr):
#     if nr > 129:
#         return True
#     else:
#         return False
# select = lambda nr: True if nr > 129 else False
# mylist = list(filter(lambda nr: True if nr > 129 else False,primes(256)))
# nr = random.randint(0,len(mylist)-1)
# print(mylist[nr])