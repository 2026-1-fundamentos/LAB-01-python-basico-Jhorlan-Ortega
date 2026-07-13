"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """
    dic = {}
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split(',')
            letra = columnas[1]   # columna 1 (índice 1)
            valor = int(columnas[2])  # columna 2 (índice 2)
            if valor not in dic:
                dic[valor] = []
            dic[valor].append(letra)
    
    # Ordenar por clave (valor) numéricamente
    resultado = sorted(dic.items())  # items devuelve tuplas (clave, lista)
    return resultado