from random import randint


def gera_numero_random():
    return [randint(1, 100) for _ in range(15)]

def bubblesort(lista):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista - 1):
        for i in range(tamanho_lista - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i+1], lista[i]
def bubble_sort_invert(list):
    tamanho_lista = len(list)
    for i in range(tamanho_lista - 1):
        for i in range(tamanho_lista - 1):
            if list[i] < list[i + 1]:
                list[i], list[i+1] = list[i+1], list[i]

list = gera_numero_random()
print(f"Lista Não Ordenada: {list}")
list.sort()
print(f"Lista Ordenada pela funcao nativa do python SORT {list}")
bubblesort(list)
print(f"Lista Ordenada pela minha funcao: {list}")
bubble_sort_invert(list)
print(f"Lista Ordenada Invertida: {list}")
