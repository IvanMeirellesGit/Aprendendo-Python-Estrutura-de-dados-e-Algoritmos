from random import randint


def gera_numero_random():
    return [randint(1, 100) for _ in range(15)]


def bubble_sort(list):
    tamanho_list = len(list)  # Tamanho da Lista
    for j in range(tamanho_list - 1):
        for i in range(tamanho_list - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]  # Troca de elementos nas posicoes i e i+1 (Exclusivo Python)

                '''
                Modo Classic:
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
                '''


list = gera_numero_random()
print(f"Lista Não Ordenada: {list}")
bubble_sort(list)
print(f"Lista Ordenada: {list}")