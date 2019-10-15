#start programa
print("*** Online kasino ***")
import numpy as np
import time, sys

#kasino gratis novac ulaz
baza = 5
ime=input("Kako se zoves?: ")
print ("Zdravo " + ime+".")
time.sleep(2)

#provjera likvidnosti
dodaj=input ("Poklanjamo ti 5KM. Koliko ti para imas " + ime+"? ")
cijena = baza + float(dodaj)
if cijena>=20:
    print ("Dobrodosao " +ime+ " idemo se igrati.")
    time.sleep(2)
    print ("***Kasino lutrija ti poklanja... ***")
    time.sleep(2)

    #kasino poklanja
    x= np.random.randint(1,1000,1)
    print (str(x))
    if x<500:
        time.sleep(2)
        print("Samo "+str(x)+" Premalo si dobio, zajebaše te.")
    
    elif x>=500:
        time.sleep(2)
        print("Uhh "+str(x)+" maraka."+" Eto para majstore.")

    #provjera stanja
    stanje=cijena+x
    print ("Na računu imaš "+str(stanje)+"KM")
    time.sleep(2)

    #ulog novca
    kocka=input("** "+ime+" koliko želiš da uložiš? ** ")
    time.sleep(1)

    if int(kocka)>stanje: 
            print (ime+" nemaš toliko para na računu.")
            #kocka=input("** "+ime+" koliko želiš da uložiš? ** ")
       
    if int(kocka)<=stanje:
            print (ime+" uložio si "+kocka+"KM.")

    #novo stanje novca
    time.sleep(2)
    stanje_novo=cijena+x-int(kocka)
    print ("*** Na računu imaš još "+str(stanje_novo)+"KM ***")
   
elif cijena<20:
    print ("Minimalan ulaz je sa 20KM. Kokuz si brate, nemas dovoljno para. Doviđenja " + ime+".")
    #kraj programa
