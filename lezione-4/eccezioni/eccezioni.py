''' 1 esempio sulle eccezioni '''
# divisione per zero

# def divisione_by_zero(dividendo, divisore):
#     try:
#         risultato = dividendo / divisore
#         return risultato
#     except ZeroDivisionError:
#         print("stai provando a dividere per zero")
#         return None

# ris = divisione_by_zero(6,0)
# print(ris)

''' 2 esempio sulle eccezioni '''
# scrivi una funzione che calcola la somma di due numeri
# def somma(a,b):
#     return a + b

# risultato = somma(4, 5)  
# print(risultato)

def somma(a,b):
    try:
        print('ciao')
    except TypeError:
        print("devono interi o float")
    else:
        print('ciao a tutti')

risultato = somma(None, 5)  
print(risultato)

# cosa succede se passiamo None? 

# def somma(a,b):
#     try:
#         if isinstance(a,str) and isinstance(b,str):
#             raise ValueError("non possono essere stringhe")
#         return a + b
#     except TypeError:
#         print("devono interi o float")
#     except ValueError as e:
#         print(f"errore {e}")


# risultato = somma(9, 9)  
# print(risultato)

# cosa succede se passiamo due stringhe?


''' 3 esempio sulle eccezioni '''
# Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola.

# def lunghezza_parole(lista_parole):
#     lunghezze = []
#     for parola in lista_parole:
#         lunghezze.append(len(parola))
#     return lunghezze

# lista_input = ["coniglio", "cane", "gatto", "barca", "gelsomino"]
# lunghezze = lunghezza_parole(lista_input)
# print(lunghezze)  # Output: [8, 4, 5, 5, 9]

# # cosa succede se la lista non ha solo stringhe ma ad esempio interi???