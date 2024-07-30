compras = []

while True:
    produto = input("Digite o produto: ")

    if produto.upper() == "FIM":
        break
    compras.append(produto)
for e in compras:
    print(e)