"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    result = []
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 4:
                col1 = columns[0]
                col4_len = len(columns[3].split(","))
                col5_len = len(columns[4].split(","))
                result.append((col1, col4_len, col5_len))
                
    return result