"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    dict = {}

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            letra = columns[0]
            valor = int(columns[1])
            if letra in dict:
                if valor > dict[letra][0] :
                    dict[letra][0] = valor
                if valor < dict[letra][1] :
                    dict[letra][1] = valor
            else:
                dict[letra] = [valor,valor]
    # Ordenar el diccionario por la clave (letra)
    ordenado = sorted(dict.items())
    resultado = []
    for item in ordenado:
        letra = item[0]
        maximo = item[1][0]
        minimo = item[1][1]
        resultado.append((letra, maximo, minimo))

    return (resultado)
