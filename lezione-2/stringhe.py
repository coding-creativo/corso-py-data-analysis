# correzione tabellina

# num = 5

# for i in range(1,11):
#     print(num, "x", i , " = ", num * i)

# for else

stringa = "oggi studiamo Python"
lettera_da_cercare = 'z'

trovato = False

for carattere in stringa:
    if carattere == lettera_da_cercare:
        trovato = True
        break


if(trovato):
    print("carattere trovato")
else:
    print("carattere non trovato")

