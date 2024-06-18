# installazione pip install numpy
# importazione import numpy as np
# differenza con le liste
# array unidimensionali
# array multidimensionali
# ndim
# zeros, ones, arange
# accedere agli elementi

import numpy as np

# Differenza con le liste
# Le liste di Python e gli array di Numpy sono simili, ma hanno alcune differenze fondamentali:
# Prestazioni: Gli array Numpy sono più efficienti in termini di memoria e velocità rispetto alle liste Python, soprattutto per grandi quantità di dati.
# Operazioni vettoriali: Gli array Numpy supportano operazioni vettoriali che permettono di effettuare calcoli su interi array senza bisogno di cicli espliciti.
# Tipi di dati omogenei: Gli array Numpy contengono elementi di un unico tipo di dato, mentre le liste Python possono contenere tipi di dati diversi.

# lista = [4,5,6,7]
# arr = np.array([4,5,6,7])
# print(type(arr))
# print(arr.ndim)
# print(arr.shape)

# print(lista)
# print(arr + 5)

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# c = np.add(a,b)
# print(c)

##------ array unidimensionali - vettore
# arr = np.array([4,5,6,7])
# print(arr[2:])

# arr[0] = 100
# print(arr)

##------ array bidimensionali - matrici
# arr_2d = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# for idx, x in np.ndenumerate(arr_2d):
#     print(idx, x)

# print(arr_2d[:,1:])

# ##------ array tridimensionali - tensor
# arr_3d = np.array([
#     [
#         [1,2],
#         [3,4]
#     ],
#     [
#         [5,6],
#         [7,8]
#     ]
# ])

# for idx, x in np.ndenumerate(arr_3d):
#     print(idx, x)

# print(arr_3d[1,1,0])

# zeros, ones, arange
zeros = np.zeros((2,4))
print(zeros)

ones = np.ones((2,4))
print(ones)

range_array = np.arange(0,101)
print(range_array)

range_array = np.arange(0,101,2)
print(range_array)