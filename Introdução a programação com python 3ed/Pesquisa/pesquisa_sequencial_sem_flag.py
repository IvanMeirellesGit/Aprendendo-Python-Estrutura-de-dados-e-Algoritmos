L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))

i = 0
while i < len(L):
    if L[i] == p:
        break
    i += 1
if i < len(L):
    print(f"{p} foi encontrado na posicao {i+1}")
else:
    print(f"{p} nao foi encontrado!")