produto1 = ["Maçã", 10, 0.30]
produto2 = ["Pera", 5, 0.75]
produto3 = ["Kiwi", 4, 0.98]

compras = [produto1, produto2, produto3]

for e in compras:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]}")
    print()