tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

print(tabela)
tabela["Tomate"] = 2.80
print(tabela["Tomate"])

print("Manga" in tabela)
print("Batata" in tabela)
print()

print(tabela.keys())
print(tabela.values())