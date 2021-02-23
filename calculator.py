#Calculator cu meniu interactiv

import datetime

while True:

    print("\nSelecteaza operatia matematica dorita.\n\n0 - Adunare\n1 - Scadere\n2 - Inmultire\n3 - Impartire\n4 - Modulo\n5 - Ridicare la putere\n6 - Radical")
    oper = input("\nOptiunea ta: ")

    #Adunare
    if oper == "0":
        val1 = float(input("\nPrima valoare: "))
        val2 = float(input("\nA doua valoare: "))
        print("\nRezultatul este: " + str(val1.__add__(val2)) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')
        if inapoi == 'y':
            continue
        else:
            break

    #Scadere
    elif oper == "1":
        val1 = float(input("\nPrima valoare: "))
        val2 = float(input("\nA doua valoare: "))
        print("\nRezultatul este: " + str(val1.__sub__(val2)) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')
        if inapoi == 'y':
            continue
        else:
            break

    #Inmultire
    elif oper == "2":
        val1 = float(input("\nPrima valoare: "))
        val2 = float(input("\nA doua valoare: "))
        print("\nRezultatul este: " + str(val1.__mul__(val2)) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')
        if inapoi == 'y':
            continue
        else:
            break

    #Impartire
    elif oper == "3":
        val1 = float(input("\nPrima valoare: "))
        val2 = float(input("\nA doua valoare: "))
        print("\nRezultatul este: " + str(val1.__truediv__(val2)) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')
        if inapoi == 'y':
            continue
        else:
            break

    #Modulo
    elif oper == "4":
        val1 = float(input("\nPrima valoare: "))
        val2 = float(input("\nA doua valoare: "))
        print("\nRezultatul este: " + str(val1.__mod__(val2)) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')
        if inapoi == 'y':
            continue
        else:
            break

    #Ridicare la putere
    elif oper == "5":
        val1 = float(input("\nValoarea bazei: "))
        val2 = float(input("\nValoarea exponentului: "))
        print("\nRezultatul este: " + str(val1.__pow__(val2)) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')
        if inapoi == 'y':
            continue
        else:
            break
    #Radical
    elif oper == "6":
        val1 = float(input("\nIntroduceti valoarea pentru extragerea radicalului: "))
        print("\nRezultatul este: " + str(val1.__pow__((1).__truediv__(2))) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')
        if inapoi == 'y':
            continue
        else:
            break


	#Cand se introduce o optiune invalida,se va crea un fisier text pe desktop si se va trece in el optiunea si datetime-ul
    else:
        a = datetime.datetime.now()
        fisier = open("C:\\Users\Mario\Desktop\data.txt", "a")
        fisier.writelines(['Utilizatorul a introdus optiunea invalida ',str(oper),' la data si ora: ',str(a),'\n','\n'])
        fisier.close()

    continue
