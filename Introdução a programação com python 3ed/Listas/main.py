lista = [0,0,0,0,0]


def input_numero():
    i = 0
    while i < len(lista):
        lista[i] = int(input(f"Número {i+1}: "))
        i += 1

def escolhe_numero(escolhido):
    i = 0
    while i < len(lista):
        i += 1
    while True:
        if escolhido == 0:
            break
        print(f"Você escolheu o numero: {lista[escolhido - 1]}")
        break

input_numero()
escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
escolhe_numero(escolhido)