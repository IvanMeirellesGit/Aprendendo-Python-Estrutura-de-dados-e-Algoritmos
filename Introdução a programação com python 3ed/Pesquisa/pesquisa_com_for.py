L = [7, 9, 10 ,12]
p = int(input("Digite um numero a pesquisar:"))

for e in L:
    if e == p:
        print("Elemento encontrado")
        break
else:
    print("elemento nao encontrado")