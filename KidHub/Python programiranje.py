import time
#ovom linijom koda smo dodali vreme u kod
ime= input("Unesi svoje ime: ")
print("Cao ", ime, " hajde da se igramo!")
time.sleep(1)
print("Pocni da pogadjas")
time.sleep(0.5)
#osmislimo rec za pogadjanje
rec="lokativ"
#promeljiva koja pamti nas pogodak
slovo=''
broj_pokusaja = 10
#petlja za pokusaje
ispis = ['_','_','_','_','_', '_', '_']
pogresan=0
while broj_pokusaja>0:
    pokusaj = input("unesi jedno slovo: ")
    slovo = pokusaj
    # nase slovo je jednako onome sto je uneto

    #ispisi crtice za svako slovo
    if slovo in rec:

        index = rec.index(slovo)
        ispis[index] = slovo
        broj_pokusaja = broj_pokusaja - 1

    else:
        pogresan+=1
        broj_pokusaja = broj_pokusaja - 1

    print(ispis)
    print("Preostali broj pokusaja je " + str(broj_pokusaja))
    print("Broj gresaka: " + str(pogresan))

    if not ispis.__contains__('_'):


        if pogresan == 0:
            print("Pobedio/la si!")
            time.sleep(3)
            break

        if pogresan > 0:
            print("Pogodio/la si rec, ali sa "  + str(pogresan) + " broj gresaka.")
            break

if ispis.__contains__('_'):
    print("Niste pobedili")