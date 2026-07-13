"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    datos = {}
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split(',')
            letra = columnas[0]
            valor = int(columnas[1])

            if letra not in datos:
                # Inicializamos con el primer valor como máximo y mínimo
                datos[letra] = {'max': valor, 'min': valor}
            else:
                if valor > datos[letra]['max']:
                    datos[letra]['max'] = valor
                if valor < datos[letra]['min']:
                    datos[letra]['min'] = valor

    # Construimos la lista de tuplas (letra, max, min) ordenada por letra
    resultado = []
    for letra in sorted(datos.keys()):
        resultado.append((letra, datos[letra]['max'], datos[letra]['min']))
    
    return resultado
