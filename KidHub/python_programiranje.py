import time
#ovom linijom koda smo dodali vreme u kod
ime= input("Unesi svoje ime: ")
print("Cao ", ime, " hajde da se igramo!")
time.sleep(1)
print("Pocni da pogadjas")
time.sleep(0.5)
#osmislimo rec za pogadjanje
rec="raskrsnica"
#promeljiva koja pamti nas pogodak
slovo=''
broj_pokusaja = 15

ispis = []
for i in range(0, len(rec)):
    ispis.append('_')

#petlja za pokusaje
pogresan = 0
while broj_pokusaja > 0:
    pokusaj = input("unesi jedno slovo: ")
    slovo = pokusaj.lower()
    # nase slovo je jednako onome sto je uneto

    #ispisi crtice za svako slovo
    if slovo in rec:
        for index in range(0, len(rec)):
            # print("IF " + slovo + " == " + rec[index : index + 1])
            if slovo == rec[index : index + 1]:
                ispis[index] = slovo
    else:
        pogresan += 1

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
