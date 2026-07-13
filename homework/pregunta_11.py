"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sumas = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split()
            if len(columns) > 3:
                valor = int(columns[1])
                letras = columns[3].split(",")
                for letra in letras:
                    sumas[letra] = sumas.get(letra, 0) + valor

    return dict(sorted(sumas.items()))
