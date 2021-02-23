import random

while True:

    a = random.randint(1,7)

    print(a)

    inapoi = input('\nVrei sa arunci zarul din nou? (y/n) ')
    if inapoi == 'y':
        continue
    else:
        break

