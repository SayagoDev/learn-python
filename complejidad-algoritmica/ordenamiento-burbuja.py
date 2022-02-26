import random

# O(n) * O(n) = O(n**2)
def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n): # O(n)
        for j in range(0, n - i - 1): # O(n)

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


if __name__ == '__main__':
    tamano_lista = int(input('De qué tamaño sera la lita? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)