def media(*numeri):
    return sum(numeri) / len(numeri)

calcolo_media = media(4,6,5)
print(calcolo_media)

def concatena(*stringhe):
    return "".join(stringhe)

ris = concatena("Ciao ", "a ", "tutti")
print(ris)

def unione_liste(*args):
    risultato = []
    for lista in args:
        risultato.extend(lista)
    return risultato

ris = unione_liste([1,2,3],[4,5],[8,9])
print(ris)

# def unione_liste(*args):
#     return [elemento for lista in args for elemento in lista]

# ris = unione_liste([1,2,3],[4,5],[8,9])
# print(ris)
# lista([1,2,3],[4,5],[8,9])

def crea_stringa(elemento, nome, *args):
    return elemento + nome + ''.join(str(args))

ris = crea_stringa('Saluti da: ', 'ciao', ['Paperino', 'Pluto', 'Pippo'])
print(ris)

def somma(a,b):
    return a + b

somma = lambda a, b: a + b
print(somma(4,5))


