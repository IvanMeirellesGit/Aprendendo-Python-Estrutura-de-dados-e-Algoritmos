lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Digite o  numero da sala (0 sai):"))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala Invalida")
    elif lugares_vagos[sala - 1] == 0:
        print("Sala Lotada!")
    else:
        lugares = int(input(f"Quantos lugares voce deseja ({lugares_vagos[sala-1]} vagos):"))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse numero de lugares nao esta disponivel!.")
        elif lugares < 0:
            print("Numero Invalido!")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
print("Ultilização de salas")

for x, l in enumerate(lugares_vagos):
    print(f"Sala: {x + 1} - {l} lugar(es) vazios(s)")