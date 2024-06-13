from math import sqrt

def ipotenusa(a, b):
    return sqrt(a**2 + b**2)

# Esempio di utilizzo della funzione
a = 3
b = 4
c = ipotenusa(a, b)
print("L'ipotenusa del triangolo rettangolo con i lati", a, "e", b, "è:", c)