L = ["a"]
print(L)
L.append("b")
print(L)
L.extend(["c"]) #metodo extend nao aceita nada que nao seja lista
print(L)
print(len(L))
L.append(["d", "e"]) #passando uma lista toda para a lista ja criada
print(L)
print(len(L))
L.extend(["f", "g"]) #passa os itens da lista para a lista ja criada
print(L)
print(len(L))

print(L[1])
print(L[3])
print(L[3][1])