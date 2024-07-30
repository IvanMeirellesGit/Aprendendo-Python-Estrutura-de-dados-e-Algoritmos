L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar (p):"))
v = int(input("Digite o outro valor a procurar (v):"))

i = 0
achouP = -1 # Aqui -1 indica que ainda nao encontramos o valor procurado
achouV = -1
primeiro = 0

while i < len(L):
    if L[i] == p:
        achouP = i
    if L[i] == v:
        achouV = i
    i += 1

if achouP != -1:
    print(f"p: {p} encontrado na posição {achouP}")
else:
    print(f"p: {p} não encontrado")

if achouV != -1:
    print(f"v: {v} encontrado na posição {achouV}")
else:
    print(f"v: {v} não encontrado")

#Verifico se ambos foram encontrados

if achouP != -1 and achouV != -1:
    #mostro a posicao de ambos
    if achouP <= achouV:
        print("P foi achado antes de V")
    else:
        print("V foi achado antes de P")