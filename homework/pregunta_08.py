"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
    (1, ['B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E']),
    (4, ['B', 'E']),
    (5, ['B', 'C', 'D', 'E']),
    (6, ['A', 'B', 'C', 'E']),
    (7, ['A', 'C', 'D', 'E']),
    (8, ['A', 'B', 'D', 'E']),
    (9, ['A', 'B', 'C', 'E'])]

    """

    dict = {}

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            letra = columns[0]
            valor = int(columns[1])
            if valor in dict:
                if letra not in dict[valor]:
                    dict[valor].append(letra)
            else:
                dict[valor] = [letra]

    # Ordenar el diccionario por la clave (letra)
    ordenado = sorted(dict.items())
    resultado = []
    for item in ordenado:
        letra = item[0]
        lista_letras = sorted(item[1])
        resultado.append((letra, lista_letras))

    return (resultado)
