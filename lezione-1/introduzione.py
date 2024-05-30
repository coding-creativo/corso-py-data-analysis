# x = 5
# y = 3.4

# nome = "Pippo"
# trovato = True


# print(x,y,nome, sep=", ")
# print("ciao da", nome)
# print("ciao da " + nome)
# print(f"ciao da {nome} - {trovato}")

# print(x, end=" ")
# print(y)

# spesa = 50
# # Calcoliamo lo sconto del 7%
# # sconto = spesa * 0.07
# # Calcoliamo l'importo da pagare
# spesa = spesa - spesa * 0.07
# spesa -= spesa * 0.07
# # Stampiamo l'importo da pagare
# print(f"Totale: {spesa:.2f} euro")

# **** type
x = 5
y = "3.4"

nome = "Pippo"
trovato = True

print(type(float(y)))
print(x+float(y))

# *** dati di input
# nome = input("Inserisci il tuo nome: ")
# print(type(nome))

# numero = int(input("inserisci un numero: "))
# print(type(numero))

# istruzioni condizionali
x = -9
if x > 0:
    print("il numero è positivo")
    print("ciao1")
elif x == 0:
    print("il numero è nullo")
    print("ciao2")
else: 
    print("il numero è negativo")

for i in range(2,10):
    print(i, end=" ")

sum = 0

for i in range(1,10):
    # sum = sum + i ---> 0 + 1  --> 1 + 2 -- > 3 + 3 ....
    sum += i

print(sum)

for car in nome:
    print(car)

numero = int(input("inserisci un numero: "))

while numero < 0:
    print("numero positivo please!!!!")
    numero = int(input("inserisci un numero: "))