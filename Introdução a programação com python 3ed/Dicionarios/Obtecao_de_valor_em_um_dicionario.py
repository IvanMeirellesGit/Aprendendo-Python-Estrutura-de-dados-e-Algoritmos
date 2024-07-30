tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

print(f"Valor da Batata: R$: {tabela['Batata']:5.2f}.")
while True:
    produto = input("Digite o nome do produto, fim para terminar:")
    if produto.upper() == "FIM":
        break
    if produto in tabela:
        print(f"Preço {tabela[produto]:5.2f}")
    else:
        print("Produto nao encontrado!")