"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    diccio = {}

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            letra = columns[0]
            diccionario = (columns[4])
            separado = diccionario.split(',')
            suma= 0
            for elemento in separado:
                pareja = elemento.split(':')
                suma += int(pareja[1])
            if letra in diccio:
                diccio[letra] += suma
            else:
                diccio[letra] = suma

    return (dict(sorted(diccio.items())))