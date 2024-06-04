dizionario = {'Nome': 'Paperino', 'Eta': 20}

# print(dizionario['a'])

# cicli sui dizionari
for chiave in dizionario:
    print(chiave, dizionario[chiave])

for chiave, valore in dizionario.items():
    print(chiave, valore)

for valore in dizionario.values():
    print(valore)

for indice, (chiave, valore) in enumerate(dizionario.items()):
    print(indice, chiave, valore)