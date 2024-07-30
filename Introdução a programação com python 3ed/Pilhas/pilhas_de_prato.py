prato = 5
pilha = list(range(1, prato + 1))

while True:
    print(f"Existem {len(pilha)} pratos na minha pilha de pratos")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar e D para Desempilhar")
    print("S para sair")
    op = input("Operação (D, E, S): ")

    if op == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} está lavado.")
        else:
            print("Pilha Vazia! Nada para lavar")
    elif op == "E":
        prato += 1
        pilha.append(prato)
    elif op == "S":
        break
    else:
        print("Operação é inválida! Digite E, D ou S!")