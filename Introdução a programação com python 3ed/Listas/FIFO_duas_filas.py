ultimo = 0
fila1 = []
fila2 = []

while True:
    print(f"Fila1 atual: {fila1}")
    print(f"Fila1 atual: {fila1}")
    print(f"Existem {len(fila1)} clientes ná fila 1 e {len(fila2)} clientes na fila 2.")
    print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),")
    print("ou A para realizar o atendimento a fila 1 (ou B para fila 2")
    print("S para sair.")
    op = input("Operação (F, G, A, B ou S):")

    i = 0
    sair = False
    while i < len(op): # faz a seleçao da fila
        if op[i] == "A" or op[i] == "F":
            fila = fila1
        else:
            fila = fila2
        if op[i] == "A" or op[i] == "B":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} foio atendido!")
            else:
                print("Fila vazia!")
        elif op[i] == "F" or op[i] == "G":
            ultimo += 1 # incrementa um ticket para novo cliente
            fila.append(ultimo)
        elif op[i] == "S":
            sair = True
            break
        else:
            print(f"Operaçao inválisa: {op[i]} na posiçao {i}! Digite apenas F, A, B, G, S!")
        i += 1
    if sair:
        break