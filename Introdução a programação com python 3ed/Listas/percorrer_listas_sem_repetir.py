primeira = []
segunda = []

while True:
    x = int(input("Digite um valor para a primeira lista (0 para sair): "))
    if x == 0:
        break
    primeira.append(x)
while True:
    x = int(input("Digite um valor para a segunda lista (0 para sair): "))
    if x == 0:
        break
    segunda.append(x)
terceira = []

duas_listas = primeira[:]
duas_listas.extend(segunda)

i = 0
while i < len(duas_listas):
    j = 0
    while j < len(terceira):
        if duas_listas[i] == terceira[j]:
            break
        j += 1
    if j == len(terceira):
        terceira.append(duas_listas[j])
    i += 1
i = 0
while i < len(terceira):
    print(f"{i}: {terceira[i]}")
    i += 1
