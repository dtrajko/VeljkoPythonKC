import random
broj = random.randint(1,20)
pokusaj = int(input("Razmisljam o broju od 1 do 20. Koji je to broj? "))
while pokusaj != broj:
	if pokusaj < broj:
		print("Vas broj je bio manji od zamisljenog.")
	else:
		print("Vas broj je bio veci od zamisljenog.")
	pokusaj = int(input("Molim vas, pokusajte ponovo. "))
print("Cestitamo! Vas broj je tacan!")
