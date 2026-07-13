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
     'jjj': 18}
    """
    conteo = {}
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split(',')
            # columna 5 (índice 4)
            col5 = columnas[4]
            # obtener las claves únicas en esta línea (usamos un set para evitar duplicados)
            claves_linea = set()
            pares = col5.split(',')
            for par in pares:
                if ':' not in par:
                    continue
                clave = par.split(':')[0].strip()
                claves_linea.add(clave)
            # incrementar el contador para cada clave presente en esta línea
            for clave in claves_linea:
                conteo[clave] = conteo.get(clave, 0) + 1

    return conteo
