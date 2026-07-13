"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    suma = 0
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                columnas = linea.split(',')
                suma += int(columnas[1])
    return suma