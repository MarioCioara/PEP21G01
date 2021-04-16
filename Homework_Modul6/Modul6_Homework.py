""" Homework 6 - needs to be presented before exam day
O fabrica de masini are nevoie de un obiect iterabil care sa contina seriile si loturile masinilor produse in ziua respectiva.
Seriile si loturile sunt numere intregi de tip int
Un lot este alcatuit din 20 de masini si primele 10 din lot sunt cu volan pe dreapta iar urmatoarele 10 cu volan pe stanga
Numerotarea loturilor incepe de la prima masina produsa cu seria 1 si lot 1
Ziua de lucru stocata in obiectul contruit de voi poate incepe cu orice numar de serie si numarul de bucati produse in acea zi poate avea orice valoare
Obiectul iterat va returna numerele loturilor din care fac parte masinile din acea zi, numerotarea lor a inceput de la prima masina produsa cu seria 0 si lot 0
Masinile cu serii pare sunt cu volan pe dreapta iar cele cu serii impare cu volan pe stanga
1)Definire: 40p
  - Creati o clasa pentru un obiect iterabil
   a) constructorul primeste doua argumente de tip int, seria de inceput si numarul de bucati. ex: (101, 41) 10p
   b) obiectul are doua metode: prima returneaza o lista cu seriile cu volan pe dreapta si a doua o lista cu seriile cu volan pe stanga 15p
   c) iterator-ul returnat de object va contine loturile din care fac parte seriile din obiectul curent  15p
2) Executie: 40p
- Creati o instanta a clasei de mai sus dand ca argumente: serie_inceput 314, bucati 90. 10p
- Iterati obiectul creat si salvati fiecare valoare din iteratie in acelas fisier pe linie noua. 30p
3) Documentatie: 20p
   a) adaugati type hints 5p
   a) documentati modulul 5p
   b) documentati clasele 5p
   c) documentati metodele 5p

"""

class CarFactory():
    '''class to track the work done'''
    left_wheel_cars = []
    right_wheel_cars = []
    left_wheel_done = []
    right_wheel_done = []

    def __init__(self,start_series: int,nr_pieces: int):
        self.start_series = start_series
        self.nr_pieces = nr_pieces

    def __iter__(self):
        all_series = []
        for series in self.left_wheel_done + self.right_wheel_done:
            all_series.extend(series)
        return CarIter(all_series)

    def lw_cars(self):
        '''method for the cars that have left hand wheel'''
        list_pieces = [] # list containing all the cars produced today
        for i in range(self.start_series,self.start_series + self.nr_pieces + 1):
            list_pieces.append(i)



        list_lot = [] # list containing the batches for each car produced
        for z in list_pieces:
            if z <= 20:
                lot = 1
                list_lot.append(lot)

            if z > 20:
                lot = z // 20 + 1
                list_lot.append(lot)

         #  containing the all cars produced today and their batches
        all = {} # dict containing the cars and their batches
        for i in list_pieces:
            for j in list_lot:

                all[i] = j
                list_lot.remove(j)
                break

        with open('cars', 'w') as file:

            file.write('Masini cu volan pe stanga: ' + '\n')
            file.write('\n')

            for x, y in all.items():
                if x % 2 == 1:
                     file.write('Masina seria: ' + str(x) + ' ' + 'Lotul:' + str(y) + '\n')

    def rw_cars(self):
        '''method for the cars that have right hand wheel'''
        list_pieces = []  # list containing all the cars produced today
        for i in range(self.start_series, self.start_series + self.nr_pieces + 1):
            list_pieces.append(i)

        list_lot = []  # list containing the batches for each car produced
        for z in list_pieces:
            if z <= 20:
                lot = 1
                list_lot.append(lot)

            if z > 20:
                lot = z // 20 + 1
                list_lot.append(lot)

        all = {}  # dict containing the cars and their batches
        for i in list_pieces:
            for j in list_lot:
                all[i] = j
                list_lot.remove(j)
                break
        with open('cars', 'a') as file:
            file.write('\n')
            file.write('Masini cu volan pe dreapta: ' + '\n')
            file.write('\n')
            for x, y in all.items():
                if x % 2 == 0:
                    file.write('Masina seria: ' + str(x) + ' ' + 'Lotul:' + str(y) + '\n')





class CarIter():
    '''Class for iterating all series'''
    def __init__(self, series: list):
        self.series = series

    def __iter__(self):
        return self

    def __next__(self):
        if not self.series:
            raise StopIteration
        else:
            return self.series.pop(0)



obj_carfactory = CarFactory(314,90)
obj_carfactory.lw_cars()
obj_carfactory.rw_cars()




