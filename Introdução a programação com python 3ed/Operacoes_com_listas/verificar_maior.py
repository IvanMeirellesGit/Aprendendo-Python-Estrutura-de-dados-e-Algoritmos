L = [1, 7, 2, 4]

maximo = L[0]
minimo = L[0]

for e in L:
    if e > maximo:
        maximo = e
    if e < minimo:
        minimo = e
print(maximo)
print(minimo)