expressao = input("Digite a sequencia de parenteses para validacao: ")

pilha = []

i = 0

while i < len(expressao):
    if expressao[i] == "(":
        pilha.append("(")
    if expressao[i] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")") #forçá a insercao e mensage de erro
            break
    i += 1
if len(pilha) == 0:
    print("Ok")
else:
    print("Erro")