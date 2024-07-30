L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar (p): "))
v = int(input("Digite o outro valor a procurar (v): "))

achouP = False
achouV = False
i = 0

primeiro_encontrado = 0

while i < len(L):
    if L[i] == p:
        achouP = True
        if not achouV:
            primeiro_encontrado = 1
    if L[i] == v:
        achouV = True
        if not achouP:
            primeiro_encontrado = 2
    i += 1
if achouP:
    print(f"P: {p} encontrado na posicao {i}")
else:
    print(f"P: {p} nao encontrado")

if achouV:
    print(f"V: {v} encontrado na posicao {i}")
else:
    print(f"V: {v} nao encontrado")

if primeiro_encontrado == 1:
    print("P foi encontrado primeiro que V")
else:
    print("V foi encontrado primeiro que P")