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
    key_values = {}
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 4:
                dict_items = columns[4].split(",")
                for item in dict_items:
                    key, val = item.split(":")
                    val = int(val)
                    if key not in key_values:
                        key_values[key] = [val, val]
                    else:
                        if val < key_values[key][0]:
                            key_values[key][0] = val
                        if val > key_values[key][1]:
                            key_values[key][1] = val
                            
    result = [(key, limits[0], limits[1]) for key, limits in key_values.items()]
    return sorted(result)
