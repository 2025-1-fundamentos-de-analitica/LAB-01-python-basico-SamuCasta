"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
    ('bbb', 1, 9),
    ('ccc', 1, 10),
    ('ddd', 0, 9),
    ('eee', 1, 7),
    ('fff', 0, 9),
    ('ggg', 3, 10),
    ('hhh', 0, 9),
    ('iii', 0, 9),
    ('jjj', 5, 17)]

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
                letra= buenos[i]
                valor=buenos[i+1]
                if letra in dict:
                    if valor > dict[letra][1] :
                        dict[letra][1] = valor
                    if valor < dict[letra][0] :
                        dict[letra][0] = valor
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


