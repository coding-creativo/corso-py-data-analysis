lista = [8,2,13]

for elemento in lista:
    print(elemento)

for index, elemento in enumerate(lista):
    print(f"indice: {index} - elemento: {elemento}")

quadrati = [x ** 2 for x in range(10)]
print(quadrati)

numeri = [1,3,4,5,8]
numeri_pari = [x for x in numeri if x % 2 == 0]
print(numeri_pari)