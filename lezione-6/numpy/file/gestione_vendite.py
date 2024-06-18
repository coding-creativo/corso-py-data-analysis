import numpy as np

data = np.loadtxt('vendite.csv', skiprows=1, delimiter=',',dtype=str)
# print(type(data))
# print(data)
# print(data.ndim)

print(data[:5])
quantita = data[:,2].astype(float)
print(quantita)

prezzo = data[:,3].astype(float)
print(prezzo)

media_q = np.mean(quantita)
print(media_q)

mediana_p = np.median(prezzo)
print(mediana_p)

dev_p = np.std(prezzo)
print(dev_p)

massimo = np.max(prezzo)
print(massimo)

prezzo_transazione = quantita * prezzo
print(prezzo_transazione)

prodotti_unici = np.unique(data[:,1])
print(prodotti_unici)

vendite = []
for prodotto in prodotti_unici:
    print(prodotto)
    vendite_prodotto = prezzo_transazione[data[:,1] == prodotto]
    # print(vendite_prodotto)
    totale_per_prodotto = np.sum(vendite_prodotto)
    print(totale_per_prodotto)
    vendite.append([prodotto, totale_per_prodotto])

print(vendite)
