"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sums = {}
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 4:
                col1 = columns[0]
                dict_items = columns[4].split(",")
                row_sum = sum(int(item.split(":")[1]) for item in dict_items)
                sums[col1] = sums.get(col1, 0) + row_sum
                
    return {key: sums[key] for key in sorted(sums.keys())}