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
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split(',')
            valor_col2 = int(columnas[1])   # columna 2 (índice 1)
            col4 = columnas[3]              # columna 4 (índice 3)
            
            # Separar por coma y obtener las letras individuales
            letras = col4.split(',')
            for letra in letras:
                letra = letra.strip()
                if letra:  # evitar vacíos
                    sumas[letra] = sumas.get(letra, 0) + valor_col2

    # Ordenar alfabéticamente las claves y construir el diccionario final
    resultado = {}
    for letra in sorted(sumas.keys()):
        resultado[letra] = sumas[letra]
    
    return resultado
