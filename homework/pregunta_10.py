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
    resultado = []
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split(',')
            letra = columnas[0]          # columna 1 (índice 0)
            col4 = columnas[3] if len(columnas) > 3 else ''   # columna 4 (índice 3)
            col5 = columnas[4] if len(columnas) > 4 else ''   # columna 5 (índice 4)

            # Contar elementos separados por coma
            cantidad_col4 = len(col4.split(',')) if col4 else 0
            cantidad_col5 = len(col5.split(',')) if col5 else 0

            resultado.append((letra, cantidad_col4, cantidad_col5))
    return resultado