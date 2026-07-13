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
    extremes = {}
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 1:
                letter = columns[0]
                value = int(columns[1])
                if letter not in extremes:
                    extremes[letter] = [value, value]
                else:
                    if value > extremes[letter][0]:
                        extremes[letter][0] = value
                    if value < extremes[letter][1]:
                        extremes[letter][1] = value
                        
    result = [(letter, ext[0], ext[1]) for letter, ext in extremes.items()]
    return sorted(result)