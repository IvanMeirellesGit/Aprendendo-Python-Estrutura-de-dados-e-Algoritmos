estoque = {"Tomate": [1000, 2.30],
           "Alface": [500, 0.45],
           "Batata": [2001, 1.20],
           "Feijao": [100,1.50],
           }

total = 0
print("Vendas: \n")
while True:
    produto = input("Nome do produto (Fim para sair): ")
    if produto.upper() == "FIM":
        break
    if produto in estoque:
        quantidade = int(input("Quantidade: "))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = quantidade * preco
            print(f"{produto}: {quantidade} X {preco} = {custo}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada nao disponivel!")
    else:
        print("Nome do produto inválido!")