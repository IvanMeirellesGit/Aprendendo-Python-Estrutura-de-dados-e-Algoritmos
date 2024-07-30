primeira = []
segunda = []

while True:
    x = int(input("Digite um numero para a primeira lista (0 para sair): "))
    if x == 0:
        break
    primeira.append(x)
while True:
    x = int(input("Digite um numero para a segunda lista (0 para sair): "))
    if x == 0:
        break
    segunda.append(x)
terceira = primeira[:]
terceira.extend(segunda)

i = 0
while i < len(terceira):
    print(f"{i}: {terceira[i]}")
    i += 1