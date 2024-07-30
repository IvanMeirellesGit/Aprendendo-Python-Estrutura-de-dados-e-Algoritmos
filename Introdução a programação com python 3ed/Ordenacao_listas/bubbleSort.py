from random import randint

def gera_lista_radom():
    return [randint(1,100) for _ in range(25)]

lista = gera_lista_radom()

tamanho_lista = len(lista)

while tamanho_lista > 1:
    troca = False
    i = 0
    while i < (tamanho_lista-1):
        if lista[i] > lista[i+1]:
            troca = True
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
        i += 1
    if not troca:
        break
    tamanho_lista -= 1
# Mostrar Lista ordenada
for e in lista:
    print(e)