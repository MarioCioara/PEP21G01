# val1 = input("\nValoarea pentru care doriti calcularea log in baza 2: ")

# Imagineaza-ti ca utilizatorul a introdus valoarea 8 și asteapta rezultatul logaritmului
import math
import datetime

val1 = 8

rezultat = math.log2(val1)

a = datetime.datetime.now()

fisier = open("C:\\Users\Mario\Desktop\da.txt","w+")
fisier.writelines(['Datetime is: ',str(a),'\n'])


print("Rezultatul este: " + str(rezultat))