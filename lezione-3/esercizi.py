# Scrivi un programma che prende in input
# una stringa e restituisce un dizionario con
# le parole come chiavi e le loro frequenze
# come valori.

testo = "Oggi coding con Python e con le funzioni"
parole = testo.split() #divide le parole e le inserisce in una lista

print(parole)

conteggio = {}

for parola in parole:
    conteggio[parola] = conteggio.get(parola, 0) + 1

print(conteggio)

# {'Oggi': 1, 'Coding': 1, 'con': 2, 'Python': 1, 'e': 1,...}