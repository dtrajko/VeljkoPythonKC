vanzemaljci = 2
lozinka = "VANZEMALJCI"
print("Brzo! Vanzemaljci napadaju planetu.")
print("Morate da aktivirate globalne odbrambene platforme.")
print("Nadam se da znate lozinku, za dobrobit Zemlje..")
print()
print("----------------------------------------------------------------")
print("          DOBRO DOSLI U GLOBALNU ODBRAMBENU MREZU               ")
print("----------------------------------------------------------------")
print()
pokusaj = input("Molim vas, ukucajte lozinku: ").upper()
while pokusaj != lozinka:
    print()
    print("!!!NEISPRAVNA LOZINKA!!!")
    print()
    vanzemaljci = vanzemaljci ** 2
    print("Sada je ", vanzemaljci, " vanzemaljaca na Zemlji. Pokusajte ponovo!")
    if vanzemaljci > 7400000000:
        break
    print()
    print("Podsetnik za lozinku: bica koja nas napadaju.")
    print()
    pokusaj = input("Brzo! Molim vas unesite lozinku: ").upper()
if vanzemaljci > 7400000000:
    print("Neeeeeeeeeee! Vanzemaljci su postali brojniji od nas. Sve je izgubljeno.")
else:
    print("Uraaaa! Pobedili smo u borbi i svet je spasen.")
