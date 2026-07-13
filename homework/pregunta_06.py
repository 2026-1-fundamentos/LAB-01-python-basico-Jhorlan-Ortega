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
    extremos = {}
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split(',')
            # La columna 5 es el índice 4
            col5 = columnas[4]
            # Dividir cada par clave:valor, separados por coma
            pares = col5.split(',')
            for par in pares:
                if ':' not in par:
                    continue
                clave, valor_str = par.split(':')
                clave = clave.strip()
                valor = int(valor_str.strip())
                if clave not in extremos:
                    extremos[clave] = [valor, valor]  # [min, max]
                else:
                    if valor < extremos[clave][0]:
                        extremos[clave][0] = valor
                    if valor > extremos[clave][1]:
                        extremos[clave][1] = valor

    # Ordenar por clave alfabéticamente y construir la lista de tuplas
    resultado = []
    for clave in sorted(extremos.keys()):
        resultado.append((clave, extremos[clave][0], extremos[clave][1]))
    return resultado