# dizionario = {'Nome': 'Paperino', 'Eta': 20}

# print(dizionario['a'])

# cicli sui dizionari
# for chiave in dizionario:
#     print(chiave, dizionario[chiave])

# for chiave, valore in dizionario.items():
#     print(chiave, valore)

# for valore in dizionario.values():
#     print(valore)

# for indice, (chiave, valore) in enumerate(dizionario.items()):
#     print(indice, chiave, valore)

dizionario = {'a': 1, 'b': 2, 'c': 3}
chiavi = dizionario.keys()
print(chiavi)
valori = dizionario.values()
print(valori)
tupla_chiavi_valori = zip(chiavi, valori)
print(list(tupla_chiavi_valori))

dizionario = {}

for chiave, valore in zip(chiavi, valori):
    print(f"chiave: {chiave} - valore {valore}")
    dizionario[chiave] = valore

print(dizionario)

frutta = {"rossa": "mela", "gialla": "melone"}
inverso = {}

for chiave, valore in frutta.items():
    inverso[valore] = chiave

print(inverso)