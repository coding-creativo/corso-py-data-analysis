def saluta():
    print("Hello WOrld!")

saluta()

def saluta(nome = 'Paperino', eta = 20):
    print(f"ciao da {nome} - ho {eta} anni")

saluta('Pippo', 24)
saluta()

def saluta(nome = None, eta = 20):
    print(f"Ciao da {nome} - ho {eta} anni")

saluta(5)

def somma(num1, num2):
    return num1 + num2

ris = somma(4,6)
print(ris)

def calcolo(num1, num2):
    return num1 + num2, num1 - num2

risultato = calcolo(4,5)
print(risultato[2])

print('ciao')


