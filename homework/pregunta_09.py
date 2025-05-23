"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
{'aaa': 13,
    'bbb': 16,
    'ccc': 23,
    'ddd': 23,
    'eee': 15,
    'fff': 20,
    'ggg': 13,
    'hhh': 16,
    'iii': 18,
    'jjj': 18}}

    """

    dict = {}

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            diccionario = columns[4]
            separado = diccionario.split(',')
            buenos= []
            for elemento in separado:
                pareja = elemento.split(':')
                buenos.append(pareja[0])
                buenos.append(int(pareja[1]))

            for i in range(0,len(buenos),2):
                letras= buenos[i]
                if letras in dict:
                    dict[letras] += 1
                else:
                    dict[letras] = 1

    return (dict)
