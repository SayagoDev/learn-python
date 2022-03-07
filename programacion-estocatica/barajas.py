import random
import collections


PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']


def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano


def escalera_color(tamano_mano, intentos):
    barajas = crear_baraja()
    manos = []

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    escalera = 0
    for mano in manos:
        palos = [carta[0] for carta in mano]
        valores = []

        if len(set(palos)) == 1:
            for carta in mano:

                try:
                    valor = int(carta[1])
                except ValueError:
                    switcher = {
                        'as': 1,
                        'jota': 11,
                        'reina': 12,
                        'rey': 13
                    }
                    valor = switcher[carta[1]]

                valores.append(valor)
                valores.sort()

                es_escalera = True
                for i, valor in enumerate(valores):
                    if i != 0:
                        if valor - valores[i-1] != 1:
                            es_escalera = False
                            break
                if es_escalera:
                    escalera += 1

    probabilidad_de_encontrar_escalera = escalera / intentos
    print(f'La probabilidad de encontrar una escalera de color en una mano de {tamano_mano} cartas es de {probabilidad_de_encontrar_escalera}')


def main(tamano_mano, intentos):
    barajas = crear_baraja()
    manos = []

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter_val = dict(collections.Counter(valores))
        for val in counter_val.values():
            if val == 2:
                pares += 1
                break

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es: {probabilidad_par}')

    escalera_color(tamano_mano, intentos)


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)