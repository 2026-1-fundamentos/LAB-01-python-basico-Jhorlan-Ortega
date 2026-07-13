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
    suma_por_letra = {}
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split(',')
            letra = columnas[0]          # columna 1 (índice 0)
            col5 = columnas[4]           # columna 5 (índice 4)
            # Dividir por comas para obtener cada par clave:valor
            pares = col5.split(',')
            for par in pares:
                if ':' not in par:
                    continue
                # Extraer el valor después del ':'
                valor_str = par.split(':')[1].strip()
                if valor_str:
                    valor = int(valor_str)
                    suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor

    # Ordenar el diccionario por clave alfabéticamente
    resultado = {}
    for letra in sorted(suma_por_letra.keys()):
        resultado[letra] = suma_por_letra[letra]
    return resultado