"""Dicionarios usam hash para cada chave contida nele.
Então sempre que procuramos uma chave no dicionario o hash é calculado
e o indicie referente aquele hash é retornado. Ele tambem lida com colisao de Hash"""

L = [0] * 10
print(L)
print(hash("A"))

print(hash("A") % 10) # Se utilizarMos o resto da divisão entre o hash e o taManho da lista, tereMos UM índice a partir da chave

L[hash("A") % 10] = "A"
print(L)