E=int(input("Unesi duzinu TV emisije u MINUTIMA: "))
E1=E*1
E2=E*2
E3=E*3
odgovor=input("Da li si poledao sve tri emisije? Odgovori sa DA ili NE: ")
if odgovor == "DA":
    raz12=abs(E1-E2)
    raz13=abs(E1-E3)
    raz23=abs(E2-E3)
    kraca=min(raz12, raz13, raz23)
    duza=max(raz12, raz13, raz23)
    print("Najduza epizoda je bila duga ",duza,"min, a najkaca ",kraca,"min.")
    U=E1+E2+E3
    minu=U%60
    h=U//60
    print("Gledao si ",h,"sati/a i ",minu," minuta.")
else:
    print("Nista onda, svrati kad budes pogledao sva tri!")
