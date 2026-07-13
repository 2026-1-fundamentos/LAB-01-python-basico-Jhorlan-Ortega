"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
    conteo = {}
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split(',')
            letra = columnas[0]  # primera columna
            conteo[letra] = conteo.get(letra, 0) + 1

    # Ordenar alfabéticamente por la letra (clave)
    resultado = sorted(conteo.items())  # items() devuelve tuplas (letra, cantidad)
    return resultado
