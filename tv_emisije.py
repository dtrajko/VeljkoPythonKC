#На ТВ-у су приказане три емисије у трајању од х1, х2 и х3 минута (вредности ће бити унете помоћу наредбе input и цели су бројеви).

х1 = int(input("Unesi duzinu prve TV emisije u minutima: "))
х2 = int(input("Unesi duzinu druge TV emisije u minutima: "))
х3 = int(input("Unesi duzinu trece TV emisije u minutima: "))

# Написати програм који ће исписати колико минута је трајала најдужа емисија, а колико најкраћа.
duza = max(х1, х2, х3)
kraca = min(х1, х2, х3)
print("Najduza emisija je trajala ", duza, " min, a najkraca ", kraca, " min.")

# Уколико је ученик гледао све три емисије, исписати колико сати и минута је провео уз ТВ.
Odgovor = input("Da li si pogledao sve 3 emisije? Odgovori sa DA ili NE: ")

if Odgovor != "DA":
	print("Nista onda, svrati opet kada budes pogledao sve.")
	quit()

U = х1 + х2 + х3
h = U // 60
minu = U % 60
print("Gledao si ", h, "h", minu, "min, ako hoces preciznije.")
