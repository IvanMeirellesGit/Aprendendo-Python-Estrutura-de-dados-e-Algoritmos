compras = []

while True:
    produto = input("Produto: ")

    if produto.upper() == "FIM":
        break

    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    compras.append([produto, quantidade, preco])

    total = 0.0

    for e in compras:
        print(f"{e[0]:20s} x {e[1]:5d} {e[2]:5.2f}. Parcial: {e[1] * e[2]:6.2f}")
        total += e[1] * e[2]
    print(f"Total: {total:7.2f}")