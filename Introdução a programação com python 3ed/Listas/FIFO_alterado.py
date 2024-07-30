ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"Existem {len(fila)} Clientes na fila.")
    print(f"Fila atual: {fila}")
    print(f"Digite (F) para add clientes\n"
          f"Digite (A) para atender clientes\n"
          f"Digite (S) para sair.")

    op = input("Operacao (F, A ou S): ")
    i = 0
    sair = False
    while i < len(op):
        if op[i] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} foi atendido.")
            else:
                print("Fila vazia. Ninguem para atender!")
        elif op[i] == "F":
            ultimo += 1
            fila.append(ultimo)
            print(f"Cliente {ultimo} entrou na fila")
        elif op[i] == "S":
            sair = True
            break
        else:
            print(f"Operaçao {op} Invalida! Digite apenas F, A ou S!")
        i += 1
    if sair:
        break